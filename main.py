import telebot
import requests
from dotenv import dotenv_values
env = {
    **dotenv_values("/home/kdev/PycharmProjects/newbot4/.env"),
    **dotenv_values(".env.dev"),  # override
}

bot = telebot.TeleBot(env["TG_BOT_TOKEN"])


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, чем я могу тебе помочь?')


@bot.message_handler(content_types=['text'])
def send_text(message):
    response = requests.post('https://api.openai.com/v1/engines/text-davinci-003/completions',
    headers={'Authorization': 'Bearer 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'},
    json={
        'prompt': message.text,
        'max_tokens': 1500
    })
    response_text = response.json()['choices'][0]['text']
    bot.send_message(message.chat.id, response_text)


bot.polling()

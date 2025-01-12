import telebot
import config
from random import choice

API_TOKEN = (config.token)

bot = telebot.TeleBot(API_TOKEN)
bf = "@BotFather"

# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, """\
Hi there, I am EchoBot.
I am here to echo your kind words back to you. Just say anything nice and I'll say the exact same thing to you!\
""")
    
# Handle all other messages with content_type 'text' (content_types defaults to ['text'])

#@bot.message_handler(func=lambda message: True)
#def echo_message(message):
#    bot.reply_to(message, message.text)

#

@bot.message_handler(commands=['info'])
def send_welcome(message):
    bot.reply_to(message, f'Я был создан учеником школы программирования Kodland при помощи {bf}')

#

@bot.message_handler(commands=['coin'])
def coin_handler(message):
    coin = choice(["ОРЕЛ", "РЕШКА"])
    bot.reply_to(message, coin)

#

@bot.message_handler(commands=['creator'])
def send_welcome(message):
    bot.reply_to(message, 'Ничего про своего разработчика не скажу. Нет возможности')

bot.infinity_polling()

import json
import telebot
from drvWebScraping import btc_scraping

usuarios={}
usuarios['manu']='5178063489'

# we are reading the token from the environmental variables of the OS
file= open('settings.json')
settings = json.load(file)

#BOT_TOKEN = os.environ.get('BOT_TOKEN')
BOT_TOKEN=settings['TOKEN']
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")

    
@bot.message_handler(commands=['dollar'])
def send_welcome(message):
    usd_prize = btc_scraping()
    user=message.chat.first_name
    text = 'Hi ' +user+ ', the prize of the usd is ' + str(usd_prize)
    bot.reply_to(message, text)


@bot.message_handler(func=lambda msg: True)
def echo_all(message):
    bot.reply_to(message, message.text)

bot.infinity_polling()


import os
from telebot import telebot
from telebot import types
from dotenv import load_dotenv
from datetime import datetime
from keyboard import *

load_dotenv()

BOT_TOKEN=BOT_TOKEN = os.getenv('BOT_TOKEN')
bot = telebot.TeleBot(BOT_TOKEN)
COMMAND_LIST = "HELP"




#Message handlers
@bot.message_handler(commands = ['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('get news')
    item2 = types.KeyboardButton('get stats')
    item3 = types.KeyboardButton('send location')
    item4 = types.KeyboardButton('send time')
    markup.add(item1, item2, item3, item4)
    bot.send_message(message.chat.id, "Welcome to our FIRENOTIFY BOT!", reply_markup=markup)
    
    
    
    
@bot.message_handler(commands=['help'])
def send_help(message):
    bot.send_message(message.chat.id, COMMAND_LIST)


bot.polling(non_stop=True)

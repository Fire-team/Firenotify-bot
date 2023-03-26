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
    bot.send_message(message.chat.id, "Welcome to our FIRENOTIFY BOT!")
@bot.message_handler(commands=['help'])
def send_help(message):
    bot.send_message(message.chat.id, COMMAND_LIST)


bot.polling()

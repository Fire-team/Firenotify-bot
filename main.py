import os
from telebot import telebot
from telebot import types
from dotenv import load_dotenv
from datetime import datetime
from keyboard import *
from visualize import visualize_incidents

load_dotenv()

BOT_TOKEN=BOT_TOKEN = os.getenv('BOT_TOKEN')
bot = telebot.TeleBot(BOT_TOKEN)
COMMAND_LIST = "HELP"




#Message handlers
@bot.message_handler(commands = ['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('get news')
    item2 = types.KeyboardButton('get graph')
    item3 = types.KeyboardButton('send location', request_location=True)
    item4 = types.KeyboardButton('send time')
    markup.add(item1, item2, item3, item4)
    bot.send_message(message.chat.id, "Welcome to our FIRENOTIFY BOT!", reply_markup=markup)


@bot.message_handler(func=lambda message: True, content_types=['location'])
def handle_location(message):
    latitude = message.location.latitude
    longitude = message.location.longitude
    bot.send_message(message.chat.id, f"Your location is ({latitude}, {longitude}).")


@bot.message_handler(func=lambda message: message.text == 'send time')
def send_time(message):
    now = datetime.now()
    time_str = now.strftime("%H:%M:%S")
    bot.send_message(message.chat.id, f"The current time is {time_str}.")


@bot.message_handler(func=lambda message: message.text == 'get graph')
def send_stats(message):
    # Call the visualize_incidents function to generate the plot and send it to the user
    plot = visualize_incidents()
    bot.send_photo(chat_id=message.chat.id, photo=plot)


@bot.message_handler(commands=['help'])
def send_help(message):
    bot.send_message(message.chat.id, COMMAND_LIST)


bot.polling(non_stop=True)

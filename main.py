import os
from telebot import telebot
from telebot import types
from dotenv import load_dotenv
from datetime import datetime
from keyboard import *


BOT_TOKEN=BOT_TOKEN = os.getenv('BOT_TOKEN')
bot = telebot.TeleBot(BOT_TOKEN)


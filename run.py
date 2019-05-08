import telebot
import config
import random
import time
import datetime
import logging
import json
import zipfile
import os
from openpyxl import Workbook
#from db_tool import DbQuery

#db_query = DbQuery()
bot = telebot.TeleBot(config.token)
logging.basicConfig(filename="sample.log", level=logging.INFO)

@bot.message_handler(regexp='/start')
def insert_into_a_db(message):
        bot.send_message(message.chat.id, "Hello there!")
pass

@bot.message_handler(content_types='text')
def default_answer(message):
    print(message.chat.id)
    bot.send_message(message.chat.id, "Шифрограмма принята. С вас {} копеек.".format(random.randint(10, 99)))
    pass
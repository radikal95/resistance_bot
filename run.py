import telebot
import config
import random
import logging
import time


#db_query = DbQuery()
bot = telebot.TeleBot(config.token)
logging.basicConfig(filename="sample.log", level=logging.INFO)

@bot.message_handler(regexp='/start')
def insert_into_a_db(message):
        bot.send_message(message.chat.id, "Hello there!")
        photo = open('cat.jpg', 'rb')
        bot.send_photo(message.chat_id, photo)
pass

@bot.message_handler(content_types='text')
def default_answer(message):
    bot.send_message(message.chat.id, "Шифрограмма принята. С вас {} копеек.".format(random.randint(10, 99)))
    bot.send_message(164930191, message.text)
    pass

while True:
    # bot.polling(none_stop=True)
    try:
        bot.polling(none_stop=True)
    except Exception as e:
        logging.error(e)
        time.sleep(15)
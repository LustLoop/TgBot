import time

import telebot
from telebot import types

from testdb import SQLighter
from config import *
import os
import output_markup
from output_markup import *


bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['game'])
def set_a_game(message):
    db = SQLighter(database_name)
    new_markup = output_markup.generate_markup()
    bot.send_message(message.chat.id, "Go katat'?", reply_markup=new_markup)
    db.close()


@bot.message_handler(commands=['start'])
def start_command(message):
    print(message.chat.username)
    bot.send_message(
        message.chat.id,
        'To join party input /join.\n' +
        'Dont even try to press /help.'
    )


@bot.message_handler(commands=['test'])
def find_file_ids(message):
    for sound in os.listdir('sounds/'):
        if sound.split('.')[-1] == 'ogg':
            f = open('sounds/' + sound, 'rb')
            bot.send_voice(message.chat.id, f, None)
        time.sleep(3)


@bot.message_handler(commands=['find'])
def find_user(message):
    db = SQLighter(database_name)
    print (db.find_user(message.chat.username))
    db.close()


@bot.message_handler(commands=['join'])
def create_new_user(message):
    db = SQLighter(database_name)
    if db.find_user(message.chat.username) is None:
        db.new_user(message.chat.id, message.chat.username)
        bot.send_message(message.chat.id, 'You\'re successfully joined this team')
    else:
        bot.send_message(message.chat.id, 'You\'re already joined this team')
    db.close()


@bot.message_handler(commands=['all'])
def print_all_users(message):
    db = SQLighter(database_name)
    print (db.count_users())
    db.close()


@bot.message_handler(commands=['send_all'])
def send_all(message):
    db = SQLighter(database_name)
    users = db.select_all()
    for user in users:
        bot.send_message(user[1], 'Everyone get in here!')
    db.close()


if __name__ == '__main__':
    bot.polling(none_stop=True)

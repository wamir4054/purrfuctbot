import telebot
import sqlite3
from telebot import types
from random import randint

bot = telebot.TeleBot("7676495696:AAFbU3lmZ1o54eH25sWit6pmk_NfA6mS-ok")
MAIN_BUTTONS = ["Получить котика"]

connection = sqlite3.connect("./database.db")
cursor = connection.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS users(chat_id INT PRIMARY KEY, existing_image_path STR)")
cursor.execute("CREATE TABLE IF NOT EXISTS images(chat_id INT PRIMARY KEY, image_path STR)")

connection.commit()
connection.close()

@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, "Привет, это бот который будет отсылать картинки с котиками по нажатию кнопки. Попробуй!", reply_markup=control_keyboard())

def createkeyboard():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    return keyboard

def control_keyboard():
    keyboard = types.InlineKeyboardMarkup(row_width=4)
    buttons = []
    button = types.InlineKeyboardButton(MAIN_BUTTONS[0], callback_data=MAIN_BUTTONS[0])
    buttons.append(button)
    keyboard.add(*buttons)
    return keyboard




bot.polling(interval=0, none_stop=True)
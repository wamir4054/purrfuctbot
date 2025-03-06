import telebot
import sqlite3
from telebot import types
from random import randint

bot = telebot.TeleBot("7676495696:AAFbU3lmZ1o54eH25sWit6pmk_NfA6mS-ok")
<<<<<<< HEAD
<<<<<<< HEAD
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
=======
main_buttons = ["Отправь котика"]

@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, "Привет, это бот который будет отсылать картинки с котиками по нажатию кнопки. Попробуй!")
>>>>>>> parent of 3e3c33b (сделал кнопку вывода котика, но пока только высылает одну картинку, также сделал кнопки которые пока только визуал)

def createkeyboard():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    return keyboard

<<<<<<< HEAD
def control_keyboard():
    keyboard = types.InlineKeyboardMarkup(row_width=4)
    buttons = []
    button = types.InlineKeyboardButton(MAIN_BUTTONS[0], callback_data=MAIN_BUTTONS[0])
    buttons.append(button)
    keyboard.add(*buttons)
    return keyboard



=======
main_buttons = ["Отправь котика"]

@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, "Привет, это бот который будет отсылать картинки с котиками по нажатию кнопки. Попробуй!")

def createkeyboard():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    return keyboard

=======
>>>>>>> parent of 3e3c33b (сделал кнопку вывода котика, но пока только высылает одну картинку, также сделал кнопки которые пока только визуал)
@bot.message_handler(func=lambda message: message.text in main_buttons)
def handlemainbuttonsselection(message):
    if message.text == main_buttons[0]:
        pass
<<<<<<< HEAD
>>>>>>> parent of 3e3c33b (сделал кнопку вывода котика, но пока только высылает одну картинку, также сделал кнопки которые пока только визуал)

bot.polling(interval=0, none_stop=True)
=======












































bot.polling(non_stop=True, interval=0)
>>>>>>> parent of 3e3c33b (сделал кнопку вывода котика, но пока только высылает одну картинку, также сделал кнопки которые пока только визуал)

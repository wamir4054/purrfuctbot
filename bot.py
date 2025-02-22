import telebot
from telebot import types

bot = telebot.TeleBot("7676495696:AAFbU3lmZ1o54eH25sWit6pmk_NfA6mS-ok")
main_buttons = ["Отправь котика"]

@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, "Привет, это бот который будет отсылать картинки с котиками по нажатию кнопки. Попробуй!")

def createkeyboard():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    return keyboard

@bot.message_handler(func=lambda message: message.text in main_buttons)
def handlemainbuttonsselection(message):
    if message.text == main_buttons[0]:
        pass












































bot.polling(non_stop=True, interval=0)

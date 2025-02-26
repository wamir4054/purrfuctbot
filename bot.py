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
=======
main_buttons = ["Отправь котика", "Инвентарь", "Перезапуск бота"]

@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, "Привет, это бот который будет отсылать картинки с котиками по нажатию кнопки. Попробуй!", reply_markup=createkeyboard(main_buttons, ))

def createkeyboard(buttons, row_width=3):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=row_width)
    keyboardbuttons = []
    for button in buttons:
        keyboardbuttons.append(button)
    keyboard.add(*keyboardbuttons)
    return keyboard


@bot.message_handler(func=lambda message: message.text in main_buttons)
def handlemainbuttonsselection(message):
    if message.text == main_buttons[0]:
        imageurl = "https://steamuserimages-a.akamaihd.net/ugc/1904477344793040639/6BBD7D304F441BFC4EE07FC1A63FEBF939A61955/?imw=512&amp;&amp;ima=fit&amp;impolicy=Letterbox&amp;imcolor=%23000000&amp;letterbox=false"
        bot.send_photo(message.chat.id, imageurl)










































<<<<<<< HEAD
=======



>>>>>>> parent of 873c6b3 (Merge branch 'pr/1')
bot.polling(non_stop=True, interval=0)

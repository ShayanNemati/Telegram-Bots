from g4f.client import Client
import telebot as tb
import os

tb.apihelper.proxy = {
    'http': 'socks5://185.107.48.7:64312',
    'https': 'socks5://185.107.48.7:64312'
}

API_TOKEN = os.getenv("API_TOKEN")

bot = tb.TeleBot(API_TOKEN)
client = Client()

@bot.message_handler(commands=["start"])
def hello_world(message):
    keyboard = tb.types.ReplyKeyboardMarkup(resize_keyboard=True,row_width=3)
    helpBtn = tb.types.KeyboardButton("Help")
    infoBtn = tb.types.KeyboardButton("Info")
    readBtn = tb.types.KeyboardButton("README")
    keyboard.add(helpBtn,infoBtn,readBtn)
    bot.send_message(message.chat.id, "How can i help you?", reply_markup=keyboard)

@bot.message_handler(func= lambda m: True)
def options(message):
    if message.text == "Help":
        bot.send_message(message.chat.id, "help!!!!!!")
    elif message.text == "Info":
        bot.send_message(message.chat.id, "Info section")
    elif message.text == "README":
        bot.send_message(message.chat.id, "read me")
    else:
        response = client.chat.completions.create(
            model = "gpt-4o-mini",
            messages = [{"role": "user", "content": message.text}],
            web_search = False
        )
        bot.send_message(message.chat.id,response.choices[0].message.content)

bot.polling()
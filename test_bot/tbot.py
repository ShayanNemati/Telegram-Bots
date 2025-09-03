from g4f.client import Client
import telebot as tb

bot = tb.TeleBot('8011470403:AAFy9APlzoND1-9SUVxgHId22FSJFFtGE-s')
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
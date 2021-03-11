import os
import telebot

TOKEN = os.environ('CHTID_hi456')
CHTID = os.environ('TOKEN_VsuhMCBot')

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
       bot.reply_to(message, f'Я бот. Приятно познакомиться, {message.from_user.first_name}')

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.from_user.id, 'Привет!')
    else:
        bot.send_message(message.from_user.id, f'Не понимаю, что это значит: {message.text}')

bot.polling(none_stop=False)


import telebot

BOT_TOKEN = '7703397897:AAGwMsn2wh54rU0jEK-VTQiUcv3vj-axpJk'
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.send_photo(message.chat.id, photo = 'https:g/santreyd.ru/upload/staff/upload/staff/vplate/all_photos/be41515f1c763aaf5ca25e13ff849520e77e231551.jpg')



bot.polling()


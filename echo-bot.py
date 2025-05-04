import telebot
import keyboards
BOT_TOKEN = '7703397897:AAGwMsn2wh54rU0jEK-VTQiUcv3vj-axpJk'
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    msg_text = message.text
    if msg_text == 'текст💬':
        bot.send_message(message.chat.id, text='Напиши подробне о том что хочешь спросить', reply_markup=keyboards.back)
    elif msg_text == 'изображение🖼':
        bot.send_message(message.chat.id, text='Опиши фотогорафию которую хочешь увидить', reply_markup=keyboards.back)
    elif msg_text == '⬅назад в меню':
        bot.send_message(message.chat.id, text='Главное меню:', reply_markup=keyboards.keyboard)
    else:
        bot.send_message(message.chat.id, text='Не распознал вашу команду', reply_markup=keyboards.keyboard)


bot.polling()


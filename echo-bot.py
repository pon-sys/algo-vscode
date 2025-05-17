import telebot
import keyboards
import fsm
BOT_TOKEN = '7703397897:AAGwMsn2wh54rU0jEK-VTQiUcv3vj-axpJk'
starter = fsm.FSM()
bot = telebot.TeleBot(BOT_TOKEN)

def handle_default_state(message):
    if message.text == 'текст💬':
        starter.set_state(message.chat.id, fsm.TEXT_STATE)
        bot.send_message(message.chat.id, text='Напиши подробне о том что хочешь спросить', reply_markup=keyboards.back)
    elif message.text == 'изображение🖼':
        starter.set_state(message.chat.id, fsm.IMAGE_STATE)
        bot.send_message(message.chat.id, text='Опиши фотогорафию которую хочешь увидить', reply_markup=keyboards.back)
    else:
        return_to_menu(message.chat.id)

    
def handle_image_state(message):
    if message.text == '⬅назад в меню':
        return_to_menu(message.chat.id)
    else:
        bot.send_message(message.chat.id, text='Начинаю генерировать изображеине...', reply_markup=keyboards.back)

def handle_text_state(message):
    if message.text == '⬅назад в меню':
        return_to_menu(message.chat.id)
    else:
        bot.send_message(message.chat.id, text='Начинаю генерировать текст...', reply_markup=keyboards.back)

def return_to_menu(chat_id):
    starter.set_state(chat_id, fsm.DEFAULT_STATE)
    bot.send_message(chat_id,'Главное меню:', reply_markup=keyboards.start)

@bot.message_handler(func=lambda message: True)
def on_mesage(message):
    state = starter.get_state(message.chat.id)
    
    if state == fsm.DEFAULT_STATE:
        handle_default_state(message)
    elif state == fsm.IMAGE_STATE:
        handle_image_state(message)
    elif state == fsm.TEXT_STATE:
        handle_text_state(message)
    else:
        return_to_menu(message.chat.id)
    

bot.polling()


# git add .
# git commit -m "update"
# git push 
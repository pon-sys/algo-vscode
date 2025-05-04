import telebot,random



text_button = telebot.types.KeyboardButton(text='текст💬')
image_button = telebot.types.KeyboardButton(text='изображение🖼')
keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
keyboard.add(image_button, text_button)


back = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
back_button = telebot.types.KeyboardButton(text='⬅назад в меню')
back.add(back_button)
import telebot

# Клавиатура для начала работы
start_kb = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
button = telebot.types.KeyboardButton(text='Мониторинг')
start_kb.add(button)

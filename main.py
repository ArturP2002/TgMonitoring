from bot_init import bot  # Импорт telegram-бота
from BotFunctions.parsing_messages import message_parsing
from telethon.sync import TelegramClient  # Класс, позволяющий подключаться к клиенту мессенджера
from telethon.tl.types import PeerChannel  # Метод, определяющий объекты типа канал/чат
import re
from secrets import api_id, api_hash, phone  # Импорт конфиденциальной информации пользователя
from BotFunctions.parsing_chats import chats_parsing
from BotFunctions.retrieve_csv_element import get_last_msg
from chat_lists import key_words, offset_id
from keyboards import start_kb
from telebot.types import Message


@bot.message_handler(commands=['start'])
def welcome(message: Message):
    """
    Функция приветствия telegram-бота
    :param message: сообщение пользователя
    """
    bot.reply_to(message, text='<b>Добро пожаловать, {name}!</b>\n\nС моей помощью вы можете проанализировать сообщения'
                               ' указанного вами telegram-канал и найти необходимые вам по ключевым словам',
                 reply_markup=start_kb,
                 parse_mode='html')
    bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)


@bot.message_handler(func=lambda message: message.text == 'Мониторинг')
def monitoring(message: Message):
    """
    Функция мониторинга telegram-канала(чата)
    :param message: сообщение пользователя
    """
    all_words = re.findall(r'\w+', str(get_last_msg()))  # Функция получения последнего отправленного сообщения
    for i_word in key_words:
        for j_word in all_words:
            if i_word.lower() == j_word.lower():
                channel_id = first_result.id  # Ник пользователя в telegram
                bot.send_message(chat_id=message.chat.id,  # ID бота
                                 text=f'<b>Было обнаружено следующее сообщение:</b> {str(get_last_msg())}\n\n<b>ID '
                                      f'канала(чата):</b> {channel_id}',
                                 parse_mode='html')  # Функция, которая пересылает сообщение
                break


if __name__ == '__main__':
    client = TelegramClient(phone, api_id, api_hash)  # Создаем наш клиент
    client.start()  # Запускаем клиент и входим в telegram-аккаунт
    first_result = chats_parsing(client)  # Результат парсинга пользователей telegram-канала(чата)
    message_parsing(client, first_result, offset_id)  # Результат парсинга сообщений telegram-канала(чата)
    bot.polling()  # Запуск бота

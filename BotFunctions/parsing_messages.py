from chat_lists import limit, all_messages, total_messages, total_count_limit
from telethon.tl.functions.messages import GetHistoryRequest  # Метод позволяющий получить сообщения пользователей
from BotFunctions.messages_save import parsing_chats_save


def message_parsing(client_tg, target_group, offset):
    """
    Функция парсинга определенного количества сообщений из telegram-канала(чата)
    :param client_tg: наш клиент
    :param target_group: целевой telegram-канал(чат)
    :param offset: необходимая для работы функции GetHistoryRequest переменная
    """
    id_list = []
    while True:
        history = client_tg(GetHistoryRequest(
            peer=target_group,
            offset_id=offset,
            offset_date=None,
            add_offset=0,
            limit=limit,
            max_id=0,
            min_id=0,
            hash=0
        ))

        if not history.messages:
            break

        messages = history.messages
        for message in messages:
            all_messages.append(message.message)
            id_list.append(message.id)
        offset = messages[len(messages) - 1].id
        if total_count_limit != 0 and total_messages >= total_count_limit:
           break

    print('\nСохраняем данные в файл...')
    parsing_chats_save(all_messages, id_list)

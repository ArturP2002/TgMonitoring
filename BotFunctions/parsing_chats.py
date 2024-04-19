from telethon.tl.functions.messages import GetDialogsRequest  # Функция, позволяющая работать с сообщениями в чате
from telethon.tl.types import InputPeerEmpty
from chat_lists import chats, size_chats, last_date, groups
from BotFunctions.chats_save import save_chats


def chats_parsing(client_tg):
    """
    Функция парсинга участников telegram-канала(чата)
    :param client_tg: наш клиент
    :return: target_group: целевой telegram-канал
    """
    result = client_tg(GetDialogsRequest(
             offset_date=last_date,
             offset_id=0,
             offset_peer=InputPeerEmpty(),
             limit=size_chats,
             hash=0
             ))
    chats.extend(result.chats)

    for chat in chats:
        groups.append(chat)

    print('Выбираем номер группы из перечня:')
    i_group = 0
    for group in groups:
        print(str(i_group) + '-' + group.title)
        if group.title == 'testing':  # Сюда пишем название канала
            break
        else:
            i_group += 1

    target_group = groups[i_group]

    print('\nУзнаём пользователей...')
    all_participants = []  # Переменная для сохранения данных пользователя
    all_participants = client_tg.get_participants(target_group)  # Функция парсинга

    print('Сохраняем данные в файл...')
    save_chats(all_participants, target_group)

    return target_group

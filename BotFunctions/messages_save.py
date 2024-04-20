import csv


def parsing_chats_save(messages_list, id_list):
    """
    Функция для сохранения последнего сообщения из telegram-канала(чат)
    """
    counter = 0
    with open("chats.csv", "w", encoding="utf-8") as chats_file:
        writer = csv.writer(chats_file, delimiter=",", lineterminator="\n")
        writer.writerow(['Сообщение', 'ID сообщения'])
        for message in messages_list:
            writer.writerow([message, id_list[counter]])
            counter += 1
    print('Парсинг сообщений группы успешно выполнен.')

import csv


def parsing_chats_save(messages_list):
    """
    Функция для сохранения последнего сообщения из telegram-канала(чат)
    """
    with open("chats.csv", "w", encoding="utf-8") as chats_file:
        writer = csv.writer(chats_file, delimiter=",", lineterminator="\n")
        for message in messages_list:
            writer.writerow([message])
    print('Парсинг сообщений группы успешно выполнен.')

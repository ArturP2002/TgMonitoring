import csv


def save_chats(saved_data, target_group):
    """
    Функция для сохранения информации о пользователях
    :param saved_data: список сохраненных данных о пользователях
    :param target_group: канал(чат) с нужной целевой задачей парсинга
    """
    with open("members.csv", "w", encoding='UTF-8') as users_file:
        writer = csv.writer(users_file, delimiter=",", lineterminator="\n")
        writer.writerow(['ID', 'Ник пользователя', 'Имя пользователя', 'Канал(чат)'])
        for user in saved_data:
            if user.id:
                user_id = user.id
            else:
                user_id = ''
            if user.username:
                username = user.username
            else:
                username = ''
            if user.first_name:
                first_name = user.first_name
            else:
                first_name = ''
            if user.last_name:
                last_name = user.last_name
            else:
                last_name = ''

            name = (first_name + ' ' + last_name).strip()
            writer.writerow([user_id, username, name, target_group.title], )
    print('Парсинг участников группы успешно выполнен.')

import csv


def retrieve_csv_element(csv_file_path, row_index, column_index):
    """
    Функция для получения последнего текстового сообщения из telegram-чата
    :param csv_file_path: файл с расширением .csv
    :param row_index: номер строки из таблицы
    :param column_index: номер колонки из таблицы
    :return: row[column_index]: сообщение из таблицы .csv
    """
    try:
        with open(csv_file_path, 'r', encoding='utf-8') as csv_file:
            csv_reader = csv.reader(csv_file)  # Открываем файл .csv для чтения
            for current_row_index, row in enumerate(csv_reader):
                if current_row_index == row_index:  # Условие для проверки строк и столбцов таблицы
                    if column_index < len(row):
                        return row[column_index]  # Вывод последнего сообщения
                    else:
                        raise ValueError(
                            f"Column index {column_index} is out of range for row {row_index}")
            raise ValueError(
                f"Row index {row_index} not found in the CSV file")
    except Exception as error:
        print(f"An error occurred: {error}")


def get_last_msg():
    """
    Функция для получения последнего отправленного сообщения в telegram-канал(чат)
    :return: element: последнее отправленное сообщение
    """
    csv_file_chats = 'chats.csv'
    row = 0
    column = 0
    element = retrieve_csv_element(csv_file_chats, row, column)
    print(element)
    return element

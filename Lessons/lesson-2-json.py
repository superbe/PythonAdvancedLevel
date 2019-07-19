import json

# ==============================================================================
# Python. Продвинутый уровень.
# Урок 2. Файловое хранение данных
# Задание 2.
#
# Исполнитель: Евгений Бабарыкин
# ==============================================================================

"""
Задание на закрепление знаний по модулю json. Есть файл orders в формате JSON 
с информацией о заказах. Написать скрипт, автоматизирующий его заполнение 
данными. Для этого:
"""


def read_order_from_json():
    """
    Прочитать файл json.
    :return: список заказов.
    """
    with open('Data/orders.json', 'r', encoding='utf-8') as f_n:
        return json.load(f_n)


def write_order_to_json(item, quantity, price, buyer, date):
    """
    Записать заказ в файл json.
    a.	Создать функцию write_order_to_json(), в которую передается 5 параметров —
    товар (item), количество (quantity), цена (price), покупатель (buyer),
    дата (date). Функция должна предусматривать запись данных в виде словаря
    в файл orders.json. При записи данных указать величину отступа в 4 пробельных
    символа;
    :param item: товар.
    :param quantity: количество.
    :param price: цена.
    :param buyer: покупатель.
    :param date: дата.
    :return: void
    """
    orders = read_order_from_json()
    orders['orders'].append(dict(item=item, quantity=quantity, price=price, buyer=buyer, date=date))
    with open('Data/orders.json', 'w', encoding='utf-8') as f_n:
        json.dump(orders, f_n, indent=4)


"""
b.	Проверить работу программы через вызов функции write_order_to_json() 
с передачей в нее значений каждого параметра.
"""
write_order_to_json('Робот lhj-46', 2, 1266, 'Петров И.', '19.07.2019')
write_order_to_json('Кукла Маша', 1, 766, 'Иванов А.', '20.07.2019')
write_order_to_json('Кукла Даша', 1, 766, 'Сидоров С.', '20.07.2019')

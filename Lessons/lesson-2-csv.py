import csv
import re

# ==============================================================================
# Python. Продвинутый уровень.
# Урок 2. Файловое хранение данных
# Задание 1.
#
# Исполнитель: Евгений Бабарыкин
# ==============================================================================

"""
Задание на закрепление знаний по модулю CSV. Написать скрипт, осуществляющий 
выборку определенных данных из файлов info_1.txt, info_2.txt, info_3.txt 
и формирующий новый «отчетный» файл в формате CSV. Для этого:
"""


def get_data():
    """
    Получить данные и преобразовать их массив массивов.
    a.	Создать функцию get_data(), в которой в цикле осуществляется перебор
    файлов с данными, их открытие и считывание данных. В этой функции
    из считанных данных необходимо с помощью регулярных выражений извлечь
    значения параметров «Изготовитель системы»,  «Название ОС», «Код продукта»,
    «Тип системы». Значения каждого параметра поместить в соответствующий список.
    Должно получиться четыре списка — например, os_prod_list, os_name_list,
    os_code_list, os_type_list. В этой же функции создать главный список
    для хранения данных отчета — например, main_data — и поместить в него
    названия столбцов отчета в виде списка: «Изготовитель системы», «Название ОС»,
    «Код продукта», «Тип системы». Значения для этих столбцов также оформить
    в виде списка и поместить в файл main_data (также для каждого файла);
    :return: полученные данные.
    """
    os_prod_list = []
    os_name_list = []
    os_code_list = []
    os_type_list = []
    developer_system_title = re.compile('Изготовитель системы')
    name_system_title = re.compile('Название ОС')
    code_system_title = re.compile('Код продукта')
    type_system_title = re.compile('Тип системы')
    get_value = re.compile(':\s+(.*)')
    for i in range(3):
        with open(f'Data/info_{i + 1}.txt', 'r', encoding='cp1251') as f:
            file_content = f.readlines()
            for record in file_content:
                if (len(developer_system_title.findall(record)) > 0):
                    os_prod_list.append(get_value.findall(record)[0])
                if (len(name_system_title.findall(record)) > 0):
                    os_name_list.append(get_value.findall(record)[0])
                if (len(code_system_title.findall(record)) > 0):
                    os_code_list.append(get_value.findall(record)[0])
                if (len(type_system_title.findall(record)) > 0):
                    os_type_list.append(get_value.findall(record)[0])

    main_data = [['Изготовитель системы', 'Название ОС', 'Код продукта', 'Тип системы']]
    for i in range(3):
        main_data.append([os_prod_list[i], os_name_list[i], os_code_list[i], os_type_list[i]])

    return main_data


def write_to_csv(file_name):
    """
    Записать данные (массив массивов) в файл csv.
    b.	Создать функцию write_to_csv(), в которую передавать ссылку на CSV-файл.
    В этой функции реализовать получение данных через вызов функции get_data(),
    а также сохранение подготовленных данных в соответствующий CSV-файл;
    :param file_name: наименование файла csv.
    :return: void
    """
    data = get_data()
    with open(file_name, 'w', encoding='utf-8') as f_n:
        f_n_writer = csv.writer(f_n)
        for row in data:
            f_n_writer.writerow(row)


def read_from_csv(file_name):
    """
    Прочитать данные из файла csv.
    :param file_name: наименование файла csv.
    :return: прочитанные данные (массив массивов).
    """
    result = []
    data = get_data()
    with open(file_name, 'r', encoding='utf-8') as f_n:
        f_n_reader = csv.reader(f_n)
        for row in f_n_reader:
            result.append(row)
            next(f_n_reader)
    return result


"""
c.	Проверить работу программы через вызов функции write_to_csv().
"""
write_to_csv('Data/main_data.csv')
print(read_from_csv('Data/main_data.csv'))

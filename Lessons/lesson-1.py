# ==============================================================================
# Python. Продвинутый уровень.
# Урок 1. Концепции хранения информации.
#
# Исполнитель: Евгений Бабарыкин
# ==============================================================================

import subprocess
import locale

"""
Вспомогательные методы
"""


def out_entity(value):
    """
    Вывести сведения о текущей сущности.
    :param value: сущность.
    :return: сформированная строка.
    """
    return f'{value}\n{type(value)}\n{len(value)}\n'


def converter(value, mode=False):
    """
    Конвертировать строку в байты или байты в строку.
    :param value: вводимая строка.
    :param mode: режим конвертирования (s - декодирование, в противном случае кодирование).
    :return: конвертированное значение.
    """
    if mode:
        return value.decode('utf-8')
    else:
        return str(value).encode('utf-8')


def ping(value):
    args = ['ping', value]
    subproc_ping = subprocess.Popen(args, stdout=subprocess.PIPE)
    for line in subproc_ping.stdout:
        line = line.decode('cp866').encode('utf-8')
        print(line.decode('utf-8'))


"""
1.	Каждое из слов «разработка», «сокет», «декоратор» представить в строковом
формате и проверить тип и содержание соответствующих переменных. Затем с помощью
онлайн-конвертера преобразовать строковые представление в формат Unicode и также
проверить тип и содержимое переменных.
"""

print('Задание 1\n')
print(out_entity('разработка'))
print(out_entity('сокет'))
print(out_entity('декоратор'))
print(out_entity('\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430'))
print(out_entity('\u0441\u043e\u043a\u0435\u0442'))
print(out_entity('\u0434\u0435\u043a\u043e\u0440\u0430\u0442\u043e\u0440'))
print()

"""
2.	Каждое из слов «class», «function», «method» записать в байтовом типе без 
преобразования в последовательность кодов (не используя методы encode и decode) 
и определить тип, содержимое и длину соответствующих переменных.
"""

print('Задание 2\n')
print(out_entity(b'class'))
print(out_entity(b'function'))
print(out_entity(b'method'))
print()

"""
3.	Определить, какие из слов «attribute», «класс», «функция», «type» невозможно 
записать в байтовом типе.
"""

print('Задание 3\n')
test1 = b'attribute'
# test1 = b'класс'
# test1 = b'функция'
test1 = b'type'
print()

"""
Слова «класс» и «функция» невозможно записать в байтовом типе.
"""

"""
4.	Преобразовать слова «разработка», «администрирование», «protocol», 
«standard» из строкового представления в байтовое и выполнить обратное 
преобразование (используя методы encode и decode).
"""

print('Задание 4\n')
print(out_entity(converter('разработка')))
print(out_entity(converter(converter('разработка'), True)))
print(out_entity(converter('администрирование')))
print(out_entity(converter(converter('администрирование'), True)))
print(out_entity(converter('protocol')))
print(out_entity(converter(b'protocol', True)))
print(out_entity(converter('standard')))
print(out_entity(converter(b'standard', True)))
print()

"""
5.	Выполнить пинг веб-ресурсов yandex.ru, youtube.com и преобразовать 
результаты из байтовового в строковый тип на кириллице.
"""

print('Задание 5\n')
ping('yandex.ru')
ping('youtube.com')
print()

"""
6.	Создать текстовый файл test_file.txt, заполнить его тремя строками: «сетевое 
программирование», «сокет», «декоратор». Проверить кодировку файла по умолчанию. 
Принудительно открыть файл в формате Unicode и вывести его содержимое.
"""

print('Задание 6\n')
def_coding = locale.getpreferredencoding()
print('По умолчанию файл откроется в кодировке: ', def_coding)
with open('test_file.txt', 'r', encoding='utf-8') as f:
    for li in f:
        print(li)

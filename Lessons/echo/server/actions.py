"""
Суть скрипта в том, чтобы сформировать список действий и вернуть на исполнение.
TODO: на последнем занятии перестроить на объекты, построить UML.
"""
from functools import reduce

"""
functools - сборник функций высокого уровня: взаимодействующих с другими функциями или возвращающие другие функции.
functools.reduce(function, iterable[, initializer]) - берёт два первых элемента, применяет к ним функцию, 
берёт значение и третий элемент, и таким образом сворачивает iterable в одно значение. Например, 
reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]) эквивалентно ((((1+2)+3)+4)+5). Если задан initializer, 
он помещается в начале последовательности.
https://pythonworld.ru/moduli/modul-functools.html
"""
from settings import INSTALLED_APPS


def get_server_actions():
    """
    Получили список действий.
    :return: список действий.
    """
    modules = reduce(
        lambda value, item: value + [__import__(f'{item}.actions')],
        INSTALLED_APPS,
        [],
    )
    """
    Формируем список модулей из зарегистрированного списка INSTALLED_APPS.
    __import__ - импортирует наименование модуля. 
    modules = [<module 'echo' from 'D:\\super_be\\Documents\\Source\\Repos\\PythonAdvancedLevel\\Lessons\\echo\\server\\echo\\__init__.py'>,
    <module 'messanger' from 'D:\\super_be\\Documents\\Source\\Repos\\PythonAdvancedLevel\\Lessons\\echo\\server\\messanger\\__init__.py'>]
    https://docs.python.org/3/library/functions.html#__import__
    """
    actions = reduce(
        lambda value, item: value + [getattr(item, 'actions', [])],
        modules,
        []
    )
    """
    Подобрали все скрипты с название 'actions'
    getattr - возвращает значение атрибута объекта.
    https://pythonz.net/references/named/getattr/
    [<module 'echo.actions' from 'D:\\super_be\\Documents\\Source\\Repos\\PythonAdvancedLevel\\Lessons\\echo\\server\\echo\\actions.py'>, 
    <module 'messanger.actions' from 'D:\\super_be\\Documents\\Source\\Repos\\PythonAdvancedLevel\\Lessons\\echo\\server\\messanger\\actions.py'>]
    """

    """
    Подобрали список контроллеров и действий 'actionnames'
    """
    return reduce(
        lambda value, item: value + getattr(item, 'actionnames', []),
        actions,
        []
    )


def resolve(action_name, actions=None):
    """
    Получить конкретное действие.
    :param action_name: наименование действия.
    :param actions: действия.
    :return: конкретное действие.
    """
    # Получили список действий.
    action_list = actions or get_server_actions()
    """
    action_list = [{'action': 'echo', 'controller': <function get_echo at 0x000000C8920907B8>}, {'action': 'send', 'controller': <function send_message at 0x000000C8920908C8>}]
    """
    action_mapping = {
        action.get('action'): action.get('controller')
        for action in action_list
    }
    """
    Сформировали словарь действий.
    {'echo': <function get_echo at 0x00000061BFCF07B8>, 'send': <function send_message at 0x00000061BFCF08C8>}
    Вернули нужный нам action_name.
    <function send_message at 0x000000E467D908C8>
    """
    return action_mapping.get(action_name)

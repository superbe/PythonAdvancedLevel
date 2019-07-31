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

    :return:
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
    return reduce(
        lambda value, item: value + getattr(item, 'actionnames', []),
        actions,
        []
    )


def resolve(action_name, actions=None):
    # Получили список действий.
    action_list = actions or get_server_actions()
    action_mapping = {
        action.get('action'): action.get('controller')
        for action in action_list
    }
    return action_mapping.get(action_name)

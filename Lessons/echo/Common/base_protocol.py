from datetime import datetime


class BaseProtocol:
    """
    Базовый класс протокола JIM.
    """
    __actions = ['presence', 'probe', 'msg', 'quit', 'authenticate', 'join', 'leave']
    """
    presence – присутствие, сервисное сообщение серверу, что клиент присутствует в сети.
    probe – проверка присутствия, сервисное сообщение сервера для проверки присутствия клиента в сети.
    msg – сообщение.
    quit – выход.
    authenticate – вход (аутентификация).
    join – присоеденится к беседе.
    leave – покинуть беседу.
    """

    def __init__(self, action='msg'):
        """
        Конструктор.
        :param action: команда протокола.
        """
        if not action:
            raise ValueError('Команда не введена.', 'action')
        if action not in self.__actions:
            raise ValueError('Введена неверная команда.', 'action')
        self.base_validate('action', action, str, 15)

        self.action = action
        self.time = datetime.now().timestamp()

    def check_action(self):
        """
        Проверить правильность заданной команды.
        :return: если команда верна, то True, в противном случае False.
        """
        return self.action in self.__actions

    @staticmethod
    def base_validate(property_name, value, type_value, length_value=0):
        """
        Проверить свойство объекта.
        :param property_name: наименование свойства.
        :param value: значение свойства.
        :param type_value: тип свойства.
        :param length_value: длина свойства в строковом представлении.
        :return:
        """
        if not type(value) is type_value:
            raise ValueError(f'Задано значение неверного типа {type(value)}. Верный тип {type_value}', property_name)
        if length_value > 0 & len(str(value)) > length_value:
            raise ValueError('Длина величины превысила допустимый предел.', property_name)

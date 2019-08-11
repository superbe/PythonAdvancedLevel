import json
from echo.Common.base_protocol import BaseProtocol


class ClientProtocol(BaseProtocol):
    """
    Класс клиентской версии протокола JIM.
    """
    user = {'account_name': '', 'status': ''}
    type = ''
    destination = ''
    sender = ''
    encoding = 'utf-8'
    room = ''
    name = ''
    message = ''

    def validate(self):
        """
        Проверить на соответствие значения протокола.
        :return: void
        """
        if not self.action:
            raise ValueError('Команда не введена.', 'action')
        if not self.check_action():
            raise ValueError('Введена неверная команда.', 'action')
        self.base_validate('action', self.action, str, 15)
        self.base_validate('time', self.time, float)
        self.base_validate('to', self.destination, str)
        self.base_validate('from', self.sender, str)
        self.base_validate('encoding', self.encoding, str)
        self.base_validate('room', self.room, str)
        self.base_validate('name', self.name, str, 25)
        self.base_validate('message', self.message, str, 500)

    def __str__(self):
        """
        Преобразовать объект в строку.
        :return: строковое представление объекта JIM.
        """
        self.validate()
        result = json.dumps({
            'action': self.action,
            'time': self.time,
            'user': self.user,
            'to': self.destination,
            'from': self.sender,
            'encoding': self.encoding,
            'room': self.room,
            'name': self.name,
            'message': self.message
        })

        if len(result) > 640:
            raise ValueError('Общая длина сообщения превысила допустимый предел.', 'json')

        return result

    def parse(self, value):
        """
        Произвести грамматический разбор строки и вернуть объект JIM.
        :param value: разбираемая строка.
        :return: объект JIM.
        """
        result = json.loads(value)
        self.action = result['action']
        self.time = result['time']
        self.user = result['user']
        self.destination = result['to']
        self.sender = result['from']
        self.encoding = result['encoding']
        self.room = result['room']
        self.name = result['name']
        self.message = result['message']

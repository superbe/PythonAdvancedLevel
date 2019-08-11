import json
from echo.Common.base_protocol import BaseProtocol


class ServerProtocol(BaseProtocol):
    """
    Класс серверной версии протокола JIM.
    """
    code = 200
    alert = ''
    error = ''
    type = ''

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
        self.base_validate('code', self.code, int)
        self.base_validate('alert', self.alert, str)
        self.base_validate('error', self.error, str)
        self.base_validate('type', self.type, str)

    def __str__(self):
        """
        Преобразовать объект в строку.
        :return: строковое представление объекта JIM.
        """
        self.validate()
        result = json.dumps({
            'action': self.action,
            'time': self.time,
            'code': self.code,
            'type': self.type,
            'alert': self.alert,
            'error': self.error
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
        self.code = result['code']
        self.type = result['type']
        self.alert = result['alert']
        self.error = result['error']

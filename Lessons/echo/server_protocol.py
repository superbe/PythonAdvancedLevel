from echo.base_protocol import BaseProtocol


class ServerProtocol(BaseProtocol):
    response = 200
    alert = ''
    error = ''

    def validate(self):
        if len(str(self.response)) > 3:
            raise ValueError('Значение кода ответа сервера вышло за допустимый предел.', 'response')
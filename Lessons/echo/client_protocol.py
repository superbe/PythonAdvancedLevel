from echo.base_protocol import BaseProtocol


class ClientProtocol(BaseProtocol):
    user = {'account_name': '', 'status': ''}
    type = ''
    to = ''
    from = ''
    encoding = 'utf-8'
    room = ''
    name = ''
    message = ''

    def validate(self):
        if len(self.message) > 500:
            raise ValueError('Длина сообщения превысила допустимый предел.', 'message')
        if len(self.name) > 25:
            raise ValueError('Длина имени пользователя или чата превысила допустимый предел.', 'name')

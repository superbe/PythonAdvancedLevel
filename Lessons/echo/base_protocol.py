from datetime import datetime


class BaseProtocol:
    __actions = [('presence', 'probe', 'msg', 'quit', 'authenticate', 'join', 'leave')]

    def __init__(self, action):
        if not action:
            raise ValueError('Команда не введена.', 'action')
        if action not in self.__actions:
            raise ValueError('Введена неверная команда.', 'action')
        if len(action) > 15:
            raise ValueError('Длина величины превысила допустимый предел.', 'action')
        self.action = action
        self.time = datetime.now().timestamp()

    def __str__(self):
        return

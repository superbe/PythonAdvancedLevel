from enum import Enum

actions = Enum('presence', 'prоbe', 'msg', 'quit', 'authenticate', 'join', 'leave')

# “action”: “presence” — присутствие. Сервисное сообщение для извещения сервера о присутствии клиента online;
# “action”: “prоbe” — проверка присутствия. Сервисное сообщение от сервера для проверки присутствии клиента online;
# “action”: “msg” — простое сообщение пользователю или в чат;
# “action”: “quit” — отключение от сервера;
# “action”: “authenticate” — авторизация на сервере;
# “action”: “join” — присоединиться к чату;
# “action”: “leave” — покинуть чат.

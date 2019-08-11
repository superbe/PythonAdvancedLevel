import socket
import json
import logging
import client_log_config
import zlib
import threading
from client_configuration import configuration, WRITE_MODE, READ_MODE
from datetime import datetime


def read(sock, buffersize):
    while True:
        response = sock.recv(buffersize)
        bytes_response = zlib.decompress(response)
        logging.info(f'Server send data "{bytes_response.decode()}"')


def make_request(action_name, data, login, destination):
    return {
        'action': action_name,
        'time': datetime.now().timestamp(),
        'data': data,
        'user': login,
        'destination': destination
    }


def main():
    try:
        logging.info('Client was started')
        sock = socket.socket()
        sock.connect((configuration.host, configuration.port))

        # Вводим имя пользователя (проработать до уатентификации и авторизации).
        # Под этим логином пользователь будет идентифицирован в сети и по этому
        # логину будут ему приходить сообщения.
        login = input('Enter login: ')

        read_thread = threading.Thread(
            target=read, args=(sock, configuration.bufferSize)
        )
        read_thread.start()

        while True:
            destination = input('Enter destination login to: ')
            data = input('Enter data: ')
            request = make_request('echo', data, login, destination)
            str_request = json.dumps(request)
            bytes_request = zlib.compress(str_request.encode())
            sock.send(bytes_request)
            logging.info(f'\nClient send data "{data}"')

    except KeyboardInterrupt:
        logging.critical('client shutdown.')


main()

import socket
import json
import logging
import client_log_config
import zlib
from client_configuration import configuration, WRITE_MODE, READ_MODE
from datetime import datetime


def make_request(action_name, data):
    return {
        'action': action_name,
        'time': datetime.now().timestamp(),
        'data': data
    }


def main():
    try:
        logging.info('Client was started')
        sock = socket.socket()
        sock.connect((configuration.host, configuration.port))
        while True:
            if configuration.mode == WRITE_MODE:
                action = input('Enter action: ')
                data = input('Enter data: ')
                request = make_request(action, data)
                str_request = json.dumps(request)
                bytes_request = zlib.compress(str_request.encode())
                sock.send(bytes_request)
                # logging.info(f'\nClient send data "{data}"')
            elif configuration.mode == READ_MODE:
                response = sock.recv(configuration.bufferSize);
                bytes_response = zlib.decompress(response)
                logging.info(f'Server send data "{bytes_response.decode()}"')
    except KeyboardInterrupt:
        logging.critical('client shutdown.')


main()

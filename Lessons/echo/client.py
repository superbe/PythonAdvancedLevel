import yaml
import socket
import json
import logging
import client_log_config
from argparse import ArgumentParser
from datetime import datetime


def main():
    parser = ArgumentParser()

    parser.add_argument('-c', '--config', type=str, required=False, help='Sets config file path')

    args = parser.parse_args()

    config = {
        'host': 'localhost',
        'port': 8000,
        'buffersize': 1024
    }

    if args.config:
        with open(args.config) as file:
            file_config = yaml.load(file, Loader=yaml.Loader)
            config.update(file_config)

    host, port = config.get('host'), config.get('port')

    try:
        logging.info('Client was started')
        sock = socket.socket()
        sock.connect((host, port))

        action = input('Enter action: ')
        data = input('Enter data: ')

        request = {
            'action': action,
            'time': datetime.now().timestamp(),
            'data': data
        }

        str_request = json.dumps(request)

        sock.send(str_request.encode())
        logging.info(f'Client send data "{data}"')

        b_response = sock.recv(config.get('buffersize')).decode();
        logging.info(f'Server send data "{b_response}"')
    except KeyboardInterrupt:
        logging.critical('client shutdown.')


main()

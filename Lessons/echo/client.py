from json import JSONDecodeError

import yaml
import socket
from argparse import ArgumentParser

from echo.client_protocol import ClientProtocol
from echo.server_protocol import ServerProtocol

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
    sock = socket.socket()
    sock.connect((host, port))
    print('Client was started')

    data = ClientProtocol()
    data.message = input('Enter data: ')
    sock.send(str(data).encode())

    print(f'Client send data "{data}"')

    response = sock.recv(config.get('buffersize')).decode();
    try:
        b_response = ClientProtocol()
        b_response.parse(response)
        print(f'Server send data "{b_response}"')
    except Exception:
        b_response = ServerProtocol()
        b_response.parse(response)
        print(f'Server send data "{b_response}"')

except KeyboardInterrupt:
    print('client shutdown.')

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
    sock.bind((host, port))
    sock.listen(5)

    print(f'Server started with {host}:{port}')

    while True:
        client, address = sock.accept()
        print(f'Client was detected {address[0]}:{address[1]}')
        try:
            b_request = ClientProtocol()
            b_request.parse(client.recv(config.get('buffersize')).decode())
            client.send(str(b_request).encode())
        except Exception:
            print('Client don\'t send message')
            request = ServerProtocol('msg')
            request.response = 500
            request.error = f'Server error. Client don\'t send message.'
            client.send(str(request).encode())
        else:
            print(f'Client send message {b_request.decode()}')
        finally:
            client.close()

except KeyboardInterrupt:
    print('Server shutdown.')

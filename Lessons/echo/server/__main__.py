import yaml
import socket
import json
import logging
import select
import server_log_config
from argparse import ArgumentParser

# from server import actions
from protocol import validate_request, make_response
from actions import resolve
from handlers import handle_default_request


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

    connections = []
    requests = []

    host, port = config.get('host'), config.get('port')

    try:
        sock = socket.socket()
        sock.bind((host, port))
        sock.setblocking(False)
        sock.settimeout(0)
        sock.listen(5)

        logging.info(f'Server started with {host}:{port}')

        while True:
            try:
                client, address = sock.accept()
                logging.info(f'Client was detected {address[0]}:{address[1]}')
                connections.append(client)
            except:
                pass

            if len(connections) > 0:
                rlist, wlist, xlist = select.select(connections, connections, connections, 0)

                for read_client in rlist:
                    bytes_request = read_client.recv(config.get('buffersize'))
                    requests.append(bytes_request)

                if requests:
                    bytes_request = requests.pop()
                    bytes_response = handle_default_request(bytes_request)

                    for write_client in wlist:
                        write_client.send(bytes_response)

    except KeyboardInterrupt:
        logging.critical('Server shutdown.')


main()

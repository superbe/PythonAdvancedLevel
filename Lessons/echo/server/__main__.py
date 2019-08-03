import yaml
import socket
import json
import logging
from argparse import ArgumentParser

# from server import actions
from protocol import validate_request, make_response
from actions import resolve

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

logger = logging.getLogger('main')
formatter = logging.Formatter('%{asctime}s - %{levelname}s - %{message}s')

file_handler = logging.FileHandler('main.log')
stream_handler = logging.StreamHandler()

file_handler.setLevel(logging.DEBUG)
stream_handler.setLevel(logging.DEBUG)

file_handler.setFormatter(formatter)
stream_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)
logger.setLevel(logging.DEBUG)

host, port = config.get('host'), config.get('port')

try:
    sock = socket.socket()
    sock.bind((host, port))
    sock.listen(5)

    logger.info(f'Server started with {host}:{port}')

    while True:
        client, address = sock.accept()
        logger.info(f'Client was detected {address[0]}:{address[1]}')

        b_request = client.recv(config.get('buffersize'))

        request = json.loads(b_request.decode())

        if validate_request(request):
            actions_name = request.get('action')
            controller = resolve(actions_name)
            if controller:
                try:
                    logger.info(f'Client send valid request {request}')
                    response = controller(request)
                except Exception as err:
                    logger.critical(f'Internal server error: {err}')
                    response = make_response(request, 500, data='Internal server error')
            else:
                logger.error(f'Controller with action name {actions_name} does not exists')
                response = make_response(request, 404, 'Action not found')
        else:
            logger.error(f'Client send invalid request {request}')
            response = make_response(request, 400, 'Wrong request')

        str_response = json.dumps(response)
        client.send(str_response.encode())

        client.close()
except KeyboardInterrupt:
    logger.critical('Server shutdown.')

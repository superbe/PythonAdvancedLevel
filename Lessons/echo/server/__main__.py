import socket
import logging
import select
import server_log_config
from handlers import handle_default_request
from server_configuration import configuration


def main():
    connections = []
    requests = []

    try:
        sock = socket.socket()
        sock.bind((configuration.host, configuration.port))
        sock.setblocking(False)
        sock.settimeout(0)
        sock.listen(5)

        logging.info(f'Server started with {configuration.host}:{configuration.port}')

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
                    bytes_request = read_client.recv(configuration.bufferSize)
                    requests.append(bytes_request)

                if requests:
                    bytes_request = requests.pop()
                    bytes_response = handle_default_request(bytes_request)

                    for write_client in wlist:
                        write_client.send(bytes_response)

    except KeyboardInterrupt:
        logging.critical('Server shutdown.')


main()

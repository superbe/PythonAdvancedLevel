import socket
import logging
import select
import server_log_config
import threading
from handlers import handle_default_request
from server_configuration import configuration


def read(sock, connections, requests, buffersize):
    try:
        bytes_request = sock.recv(buffersize)
    except Exception:
        connections.remove(sock)
    else:
        requests.append(bytes_request)


def write(sock, connections, response):
    try:
        sock.send(response)
    except Exception:
        connections.remove(sock)


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
                    read_thread = threading.Thread(
                        target=read, args=(read_client, connections, requests, configuration.bufferSize)
                    )
                    read_thread.start()

                if requests:
                    bytes_request = requests.pop()
                    bytes_response = handle_default_request(bytes_request)

                    for write_client in wlist:
                        write_thread = threading.Thread(
                            target=write, args=(write_client, connections, bytes_response)
                        )
                        write_thread.start()

    except KeyboardInterrupt:
        logging.critical('Server shutdown.')


main()

import yaml
from argparse import ArgumentParser


class ServerConfiguration:
    """
    Класс конфигурирования сервера.
    """
    # Наподумать. Возможно необходимо вынести общие свойства и методы в общий базовый класс, либо как-то реализовать
    # через обертку.
    _host = 'localhost'
    _port = 8000
    _bufferSize = 1024
    __instance = None

    def __init__(self):
        """
        Конструктор.
        """
        parser = ArgumentParser()
        parser.add_argument('-c', '--config', type=str, required=False, help='Sets config file path')
        args = parser.parse_args()
        config = {'host': 'localhost', 'port': 8000, 'buffer_size': 1024}
        if args.config:
            with open(args.config) as file:
                config = yaml.load(file, Loader=yaml.Loader)
                self._host, self._port, self._bufferSize = config.get('host'), config.get('port'), config.get(
                    'buffer_size')

    @classmethod
    def getInstance(cls):
        """
        Получить экземпляр конфигурации сервера.
        :return: экземпляр конфигурации сервера.
        """
        # Реализуем синглтон.
        if not cls.__instance:
            cls.__instance = ServerConfiguration()
        return cls.__instance

    @property
    def host(self):
        """
        Хост.
        :return: значение хоста.
        """
        return self._host

    @host.setter
    def host(self, value):
        """
        Хост.
        :param value: значение хоста.
        :return: void
        """
        self._host = value

    @host.deleter
    def host(self):
        """
        Хост.
        :return: void
        """
        del self._host

    @property
    def port(self):
        """
        Порт.
        :return: значение порта.
        """
        return self._port

    @port.setter
    def port(self, value):
        """
        Порт.
        :param value: значение порта.
        :return: void
        """
        self._port = value

    @port.deleter
    def port(self):
        """
        Порт.
        :return: void
        """
        del self._port

    @property
    def bufferSize(self):
        """
        Размер буфера.
        :return: значение размера буфера.
        """
        return self._bufferSize

    @bufferSize.setter
    def bufferSize(self, value):
        """
        Размер буфера.
        :param value: значение размера буфера.
        :return: void
        """
        self._bufferSize = value

    @bufferSize.deleter
    def bufferSize(self):
        """
        Размер буфера.
        :return: void
        """
        del self._bufferSize


configuration = ServerConfiguration.getInstance()

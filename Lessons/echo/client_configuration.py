import yaml
from argparse import ArgumentParser

WRITE_MODE = 'write'
READ_MODE = 'read'


class ClientConfiguration:
    """
    Класс конфигурирования клиента.
    """
    # Наподумать. Возможно необходимо вынести общие свойства и методы в общий базовый класс, либо как-то реализовать
    # через обертку.
    _host = 'localhost'
    _port = 8000
    _bufferSize = 1024
    _mode = 'write'
    __instance = None

    def __init__(self):
        """
        Конструктор.
        """
        parser = ArgumentParser()
        parser.add_argument('-c', '--config', type=str, required=False, help='Sets config file path')
        parser.add_argument('-m', '--mode', type=str, default=WRITE_MODE, help='Sets client mode')
        args = parser.parse_args()
        config = {'host': 'localhost', 'port': 8000, 'buffer_size': 1024}
        if args.config:
            with open(args.config) as file:
                config = yaml.load(file, Loader=yaml.Loader)
                self._host, self._port, self._bufferSize = config.get('host'), config.get(
                    'port'), config.get(
                    'buffer_size')
        if args.mode:
            self._mode = args.mode

    @classmethod
    def getInstance(cls):
        """
        Получить экземпляр конфигурации клиента.
        :return: экземпляр конфигурации клиента.
        """
        # Реализуем синглтон.
        if not cls.__instance:
            cls.__instance = ClientConfiguration()
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

    @property
    def mode(self):
        """
        Режим запуска клиента.
        :return: значение режима запуска клиента.
        """
        return self._mode

    @mode.setter
    def mode(self, value):
        """
        Режим запуска клиента.
        :param value: значение режима запуска клиента.
        :return: void
        """
        self._mode = value

    @mode.deleter
    def mode(self):
        """
        Режим запуска клиента.
        :return: void
        """
        del self._mode


configuration = ClientConfiguration.getInstance()

import logging
from framework.singleton.singleton import Singleton


class BaseLogger(metaclass=Singleton):
    _logger = None

    def __init__(self, level=logging.INFO):
        self._logger = logging.getLogger(__name__)
        self.fileHandler = logging.FileHandler("logfile.log", encoding="utf-8", mode="w")
        self.formatter = logging.Formatter(fmt="%(levelname)s (%(asctime)s) : %(message)s  [%(filename)s] "
                                               "(Line: %(lineno)d)", datefmt="%d.%m.%Y %H:%M:%S")
        self._logger.addHandler(self.fileHandler)
        self._logger.setLevel(level)
        self.fileHandler.setFormatter(self.formatter)

    def _get_logger(self):
        return self._logger

    @staticmethod
    def debug(msg: str):
        """Оставляет сообщение в лог уровня debug"""
        BaseLogger()._get_logger().debug(msg)

    @staticmethod
    def info(msg: str):
        """Оставляет сообщение в лог уровня info"""
        BaseLogger()._get_logger().info(msg)

    @staticmethod
    def warning(msg: str):
        """Оставляет сообщение в лог уровня warning"""
        BaseLogger()._get_logger().warning(msg)

    @staticmethod
    def error(msg: str):
        """Оставляет сообщение в лог уровня error"""
        BaseLogger()._get_logger().error(msg)

    @staticmethod
    def critical(msg: str):
        """Оставляет сообщение в лог уровня critical"""
        BaseLogger()._get_logger().error(msg)

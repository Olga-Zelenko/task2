from selenium import webdriver
from utilities import settings
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from logger import logger
from enum import Enum


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        else:
            cls._instances[cls].__init__(*args, **kwargs)
        return cls._instances[cls]


class Browser(metaclass=Singleton):
    def __init__(self, options, wed_driver):
        logger.info(f"Задаем параметры браузера")
        self.options = options
        logger.info(f"Инициализируем браузер")
        self.driver = wed_driver

    def close_browser(self):
        logger.info(f"Закрываем браузер {__class__.__name__}")
        self.driver.quit()
        logger.info(f"Обнуляем экземпляр браузер {__class__.__name__}")
        self.driver = None


class Chrome(Browser, metaclass=Singleton):
    def __init__(self):
        logger.info(f"Запускаем браузер - {__class__.__name__}")
        super().__init__(webdriver.ChromeOptions(), webdriver.Chrome(options=webdriver.ChromeOptions()))


class FireFox(Browser, metaclass=Singleton):

    def __init__(self):
        logger.info(f"Запускаем браузер - {__class__.__name__}")
        super().__init__(webdriver.FirefoxOptions(), webdriver.Firefox(options=webdriver.FirefoxOptions()))


class FactoryBrowser:
    @staticmethod
    def create_browser(type_browser: str):
        factory_dict = {
            "Chrome": Chrome,
            "FireFox": FireFox
        }
        logger.info(f"Выбираем браузер для запуска - {type_browser}")
        try:
            return factory_dict[type_browser]()
        except KeyError:
            print(f"Неизвестный браузер - {type_browser}")


driver = FactoryBrowser.create_browser(settings.browser()).driver
action = ActionChains(driver)
wait = WebDriverWait(driver, settings.timeout())

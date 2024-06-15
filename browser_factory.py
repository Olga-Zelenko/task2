from selenium import webdriver
from utilities import ParsingData

from logger import logger


class FactoryBrowser:
    @staticmethod
    def create_browser(browser_name: str = ParsingData.chrome):
        logger.info(f"Выбираем браузер для запуска - {browser_name}")
        if browser_name == "Chrome":
            driver = webdriver.Chrome()
        elif browser_name == "FireFox":
            driver = webdriver.Firefox()
        else:
            raise ValueError(f"Передан некорректный браузер {browser_name}")
        return driver

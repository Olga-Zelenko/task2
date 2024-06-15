from selenium import webdriver

from logger import logger


class FactoryBrowser:
    @staticmethod
    def create_browser(browser_name: str = "Chrome"):
        logger.info(f"Выбираем браузер для запуска - {browser_name}")
        if browser_name == "Chrome":
            driver = webdriver.Chrome()
        elif browser_name == "Firefox":
            driver = webdriver.Firefox()
        else:
            raise ValueError(f"Передан некорректный браузер {browser_name}")
        return driver

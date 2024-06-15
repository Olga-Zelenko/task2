from typing import Optional

from selenium.webdriver.remote.webdriver import WebDriver


class SingletonWebDriver:
    __instance = None

    def __new__(cls, driver: WebDriver = None) -> Optional[WebDriver]:
        if cls.__instance is None and driver:
            cls.__instance = driver
        return cls.__instance

    @classmethod
    def clear_instance(cls):
        cls.__instance = None
        return cls.__instance

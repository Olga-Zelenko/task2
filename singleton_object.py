from typing import Optional

from selenium.webdriver.remote.webdriver import WebDriver


class SingletonWebDriver:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not isinstance(cls.__instance, cls):
            cls.__instance = object.__new__(cls)
        return cls.__instance

    @classmethod
    def clear_instance(cls):
        cls.__instance = None
        return cls.__instance

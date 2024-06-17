from .base_element import BaseElement
from logger import logger


class Button(BaseElement):
    def __init__(self, locator, name):
        super().__init__(locator, name)

    def submit_element(self):
        logger.info(f"Отправляем заполненную форму нажатием на {self.name}")
        self.find_element().submit()

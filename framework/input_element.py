from .base_element import BaseElement
from logger import logger


class InputElement(BaseElement):
    def __init__(self, locator, name):
        super().__init__(locator, name)

    def send_keys_input(self, text):
        logger.info(f"Очищаем форму {self.name}")
        self.find_element().clear()
        logger.info(f"Вводим в форму {self.name}: '{text}'")
        self.find_element().send_keys(text)

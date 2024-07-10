from framework.elements.base_element import BaseElement
from framework.logger.logger import BaseLogger


class TextField(BaseElement):
    def __init__(self, locator, name):
        super().__init__(locator, name)

    def send_keys_input(self, text):
        self.find_element().clear()
        BaseLogger.info(f"Вводим в форму {self.name}: '{text}'")
        self.find_element().send_keys(text)

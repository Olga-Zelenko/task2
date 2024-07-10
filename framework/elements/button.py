from framework.elements.base_element import BaseElement
from framework.logger.logger import BaseLogger


class Button(BaseElement):
    def __init__(self, locator, name):
        super().__init__(locator, name)

    def submit_element(self):
        BaseLogger.info(f"Отправляем заполненную форму нажатием на {self.name}")
        self.find_element().submit()

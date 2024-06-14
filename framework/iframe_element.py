from .base_element import BaseElement
from logger import logger
from driver import driver


class IframeElement(BaseElement):
    def __init__(self, locator, name):
        super().__init__(locator, name)

    def find_and_switch_to_iframe(self):
        frame = self.find_element()
        logger.info(f"Переключаемся на frame '{self.name}'")
        driver.switch_to.frame(frame)

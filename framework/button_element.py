from .base_element import BaseElement


class ButtonElement(BaseElement):
    def __init__(self, locator, name):
        super().__init__(locator, name)


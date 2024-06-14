from .base_element import BaseElement


class ContainerElement(BaseElement):
    def __init__(self, locator, name):
        super().__init__(locator, name)


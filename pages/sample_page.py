from .base_page import BasePage


class SamplePage(BasePage):
    def __init__(self):
        super().__init__("//*[@id='sampleHeading']", "Uniq element - title")

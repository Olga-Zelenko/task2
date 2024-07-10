from framework.base_page.base_page import BasePage
from framework.browser.browser import Browser


class SamplePage(BasePage):
    __UNIQ_ELEM_LOCATOR = "//*[@id='sampleHeading']"

    def __init__(self):
        super().__init__(self.__UNIQ_ELEM_LOCATOR, "Uniq element - title")

    def close_current_window(self):
        Browser().close_current_window()

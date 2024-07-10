from framework.base_page.base_page import BasePage
from framework.elements.link import Link
from framework.browser.browser import Browser


class LinksPage(BasePage):
    __HOME_LINK = Link("//*[@id='simpleLink']", "Home link")
    __UNIQ_ELEM_LOCATOR = "//*[@id='linkWrapper']"

    def __init__(self):
        super().__init__(self.__UNIQ_ELEM_LOCATOR, "Links form")

    def click_home_link(self):
        self.__HOME_LINK.click_element()

    def window_handles(self):
        return Browser().window_handles()

    def switch_to_window(self, name_window):
        return Browser().switch_to_window(name_window)

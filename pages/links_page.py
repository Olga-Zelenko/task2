from .base_page import BasePage
from framework.link_element import Link


class LinksPage(BasePage):
    __HOME_LINK = ("//*[@id='simpleLink']", "Home link")

    def __init__(self):
        super().__init__("//*[@id='linkWrapper']", "Links form")

    def click_home_link(self):
        Link(*self.__HOME_LINK).click_element()

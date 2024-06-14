from .base_page import BasePage
from framework.link_element import LinkElement


class LinksPage(BasePage):
    def __init__(self):
        super().__init__("//*[@id='linkWrapper']", "Links form")

    __Home_link = LinkElement("//*[@id='simpleLink']", "Home link")

    def click_home_link(self):
        self.__Home_link.click_element()

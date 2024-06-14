from .base_page import BasePage
from framework.button_element import ButtonElement
from forms_pages.left_menu_form import LeftMenuForm


class BrowserWindowsPage(BasePage):
    def __init__(self):
        super().__init__("//*[@id='browserWindows']", 'Browser windows form')

    __New_tab_btn = ButtonElement("//*[@id='tabButton']", "New tab btn")

    left_menu = LeftMenuForm()

    def click_new_tab_btn(self):
        self.__New_tab_btn.click_element()

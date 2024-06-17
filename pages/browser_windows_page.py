from .base_page import BasePage
from framework.button_element import Button
from forms_pages.left_menu_form import LeftMenuForm


class BrowserWindowsPage(BasePage):
    __NEW_TAB_BTN = ("//*[@id='tabButton']", "New tab btn")

    __left_menu = LeftMenuForm()

    @property
    def left_menu(self):
        return self.__left_menu

    def __init__(self):
        super().__init__("//*[@id='browserWindows']", "Browser windows form")

    def click_new_tab_btn(self):
        Button(*self.__NEW_TAB_BTN).click_element()

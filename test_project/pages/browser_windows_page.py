from framework.base_page.base_page import BasePage
from framework.elements.button import Button
from test_project.forms.left_menu_form import LeftMenuForm
from framework.browser.browser import Browser


class BrowserWindowsPage(BasePage):
    __NEW_TAB_BTN = Button("//*[@id='tabButton']", "New tab btn")
    __UNIQ_ELEM_LOCATOR = "//*[@id='browserWindows']"

    __left_menu = LeftMenuForm()

    @property
    def left_menu(self):
        return self.__left_menu

    def __init__(self):
        super().__init__(self.__UNIQ_ELEM_LOCATOR, "Browser windows form")

    def click_new_tab_btn(self):
        self.__NEW_TAB_BTN.click_element()

    def window_handles(self):
        return Browser().window_handles()

    def switch_to_window(self, name_window):
        return Browser().switch_to_window(name_window)

    def get_relative_link(self):
        return Browser().get_relative_link()

from framework.base_page.base_page import BasePage
from test_project.forms.left_menu_form import LeftMenuForm


class AlertsWindowsPage(BasePage):
    __left_menu = LeftMenuForm()
    __UNIQ_ELEM_LOCATOR = "//*[contains(@class,'show')]//*[contains(text(),'Alerts')]"

    @property
    def left_menu(self):
        return self.__left_menu

    def __init__(self):
        super().__init__(self.__UNIQ_ELEM_LOCATOR, "Uniq element - show item Alerts")

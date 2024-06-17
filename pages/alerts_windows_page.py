from .base_page import BasePage
from forms_pages.left_menu_form import LeftMenuForm


class AlertsWindowsPage(BasePage):
    __left_menu = LeftMenuForm()

    @property
    def left_menu(self):
        return self.__left_menu

    def __init__(self):
        super().__init__(
            "//*[contains(@class,'show')]//*[contains(text(),'Alerts')]",
            "Uniq element - show item Alerts",
        )

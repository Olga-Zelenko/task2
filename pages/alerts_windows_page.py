from .base_page import BasePage
from forms_pages.left_menu_form import LeftMenuForm


class AlertsWindowsPage(BasePage):
    def __init__(self):
        super().__init__("//*[contains(@class,'show')]//*[contains(text(),'Alerts')]",
                         "Uniq element - show item Alerts")

    left_menu = LeftMenuForm()

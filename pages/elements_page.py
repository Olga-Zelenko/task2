from .base_page import BasePage
from forms_pages.left_menu_form import LeftMenuForm


class ElementsPage(BasePage):
    def __init__(self):
        super().__init__("//*[contains(@class,'show')]//*[contains(text(),'Web Tables')]", "Uniq element - show item "
                                                                                           "Web Table")

    left_menu = LeftMenuForm()

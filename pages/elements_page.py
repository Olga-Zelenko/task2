from .base_page import BasePage
from forms_pages.left_menu_form import LeftMenuForm


class ElementsPage(BasePage):
    __left_menu = LeftMenuForm()

    @property
    def left_menu(self):
        return self.__left_menu

    def __init__(self):
        super().__init__(
            "//*[contains(@class,'show')]//*[contains(text(),'Web Tables')]",
            "Uniq element - show item " "Web Table",
        )

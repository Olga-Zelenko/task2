from framework.button_element import Button
from pages.base_page import BasePage


class LeftMenuForm(BasePage):

    __ELEMENTS_MENU = Button(
        "//*[@class='header-wrapper']//*[contains(text(),'Elements')]", "Elements menu"
    )
    __WEB_TABLES_MENU_ITEM = Button(
        "//*[@id='item-3']//*[contains(text(),'Web Tables')]", "Menu item - Alerts"
    )
    __LINKS_MENU_ITEM = Button(
        "//*[@id='item-5']//*[contains(text(),'Links')]", "Menu item - Links"
    )
    __ALERTS_MENU_ITEM = Button(
        "//*[@id='item-1']//*[contains(text(),'Alerts')]", "Menu item - Alerts"
    )
    __NESTED_FRAMES_ITEM = Button(
        "//*[@id='item-3']//*[contains(text(),'Nested Frames')]",
        "Menu item - " "Nested frames",
    )
    __FRAMES_ITEM = Button(
        "//*[@id='item-2']//*[contains(text(),'Frames')]", "Menu item - Frames"
    )
    __BROWSER_WINDOWS_ITEM = Button(
        "//*[@id='item-0']//*[contains(text(),'Browser Windows')]",
        "Menu item - Browser Windows",
    )

    def __init__(self):
        super().__init__("//*[contains(@class,'left-pannel')]", "Left menu form")

    def click_alerts_menu_item(self):
        self.__ALERTS_MENU_ITEM.click_element()

    def click_nested_frames_menu_item(self):
        self.__NESTED_FRAMES_ITEM.click_element()

    def click_frames_menu_item(self):
        self.__FRAMES_ITEM.click_element()

    def click_browser_windows_menu_item(self):
        self.__BROWSER_WINDOWS_ITEM.click_element()

    def click_web_tables_menu_item(self):
        self.__WEB_TABLES_MENU_ITEM.click_element()

    def click_links_menu_item(self):
        self.__LINKS_MENU_ITEM.click_element()

    def click_elements_menu(self):
        self.__ELEMENTS_MENU.click_element()

    def wait_visibility_links_item(self):
        self.__LINKS_MENU_ITEM.wait_visibility_element()

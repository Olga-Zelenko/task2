from framework.button_element import ButtonElement


class LeftMenuForm:
    __Elements_menu = ButtonElement(
        "//*[@class='header-wrapper']//*[contains(text(),'Elements')]", "Elements menu"
    )
    __Web_tables_menu_item = ButtonElement(
        "//*[@id='item-3']//*[contains(text(),'Web Tables')]", "Menu item - Alerts"
    )
    __Links_menu_item = ButtonElement(
        "//*[@id='item-5']//*[contains(text(),'Links')]", "Menu item - Links"
    )
    __Alerts_menu_item = ButtonElement(
        "//*[@id='item-1']//*[contains(text(),'Alerts')]", "Menu item - Alerts"
    )
    __Nested_frames_item = ButtonElement(
        "//*[@id='item-3']//*[contains(text(),'Nested Frames')]",
        "Menu item - " "Nested frames",
    )
    __Frames_item = ButtonElement(
        "//*[@id='item-2']//*[contains(text(),'Frames')]", "Menu item - Frames"
    )
    __Browser_windows_item = ButtonElement(
        "//*[@id='item-0']//*[contains(text(),'Browser Windows')]",
        "Menu item - Browser Windows",
    )

    def click_alerts_menu_item(self):
        self.__Alerts_menu_item.click_element()

    def click_nested_frames_menu_item(self):
        self.__Nested_frames_item.click_element()

    def click_frames_menu_item(self):
        self.__Frames_item.click_element()

    def click_browser_windows_menu_item(self):
        self.__Browser_windows_item.click_element()

    def click_web_tables_menu_item(self):
        self.__Web_tables_menu_item.click_element()

    def click_links_menu_item(self):
        self.__Links_menu_item.click_element()

    def click_elements_menu(self):
        self.__Elements_menu.click_element()

    def wait_visibility_links_item(self):
        self.__Links_menu_item.wait_visibility_element()

from .base_page import BasePage
from framework.button_element import ButtonElement
from framework.container_element import ContainerElement


class AlertsPage(BasePage):
    def __init__(self):
        super().__init__("//*[@id='javascriptAlertsWrapper']", "Alerts form")

    __Btn_click_alert = ButtonElement("//*[@id='alertButton']", "Click Button to see alert")
    __Btn_click_confirm_box = ButtonElement("//*[@id='confirmButton']", "Click button to appear confirm box")
    __Message_confirm_box = ContainerElement("//*[@id='confirmResult']", "Message about selected in confirm box")
    __Btn_click_prompt_box = ButtonElement("//*[@id='promtButton']", "Click button to see prompt box")
    __Message_prompt_box = ContainerElement("//*[@id='promptResult']", "Message about entered in prompt box")

    def click_btn_to_see_alert(self):
        self.__Btn_click_alert.click_element()

    def click_btn_confirm_box(self):
        self.__Btn_click_confirm_box.click_element()

    def getting_text_message_confirm_box(self):
        return self.__Message_confirm_box.getting_text_element()

    def click_btn_prompt_box(self):
        self.__Btn_click_prompt_box.click_element()

    def getting_text_message_prompt_box(self):
        return self.__Message_prompt_box.getting_text_element()

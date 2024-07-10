from framework.base_page.base_page import BasePage
from framework.elements.button import Button
from framework.elements.text_box import TextBox
from framework.browser.browser import Browser


class AlertsPage(BasePage):
    __BTN_CLICK_ALERT = Button("//*[@id='alertButton']", "Click Button to see alert")
    __BTN_CLICK_CONFIRM_BOX = Button("//*[@id='confirmButton']", "Click button to appear confirm box")
    __MESSAGE_CONFIRM_BOX = TextBox("//*[@id='confirmResult']", "Message about selected in confirm box")
    __BTN_CLICK_PROMPT_BOX = Button("//*[@id='promtButton']", "Click button to see prompt box")
    __MESSAGE_PROMPT_BOX = TextBox("//*[@id='promptResult']", "Message about entered in prompt box")
    __UNIQ_ELEM_LOCATOR = "//*[@id='javascriptAlertsWrapper']"

    def __init__(self):
        super().__init__(self.__UNIQ_ELEM_LOCATOR, "Alerts form")

    def click_btn_to_see_alert(self):
        self.__BTN_CLICK_ALERT.click_element()

    def click_btn_confirm_box(self):
        self.__BTN_CLICK_CONFIRM_BOX.click_element()

    def getting_text_message_confirm_box(self):
        return self.__MESSAGE_CONFIRM_BOX.getting_text_element()

    def click_btn_prompt_box(self):
        self.__BTN_CLICK_PROMPT_BOX.click_element()

    def getting_text_message_prompt_box(self):
        return self.__MESSAGE_PROMPT_BOX.getting_text_element()

    def getting_text_alert(self):
        return Browser().switch_alert().text

    def accept_alert(self):
        Browser().switch_alert().accept()

    def getting_list_frame(self):
        return Browser().window_handles()

    def send_keys_alert(self, text):
        Browser().switch_alert().send_keys(text)

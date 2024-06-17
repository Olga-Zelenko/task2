from .base_page import BasePage
from framework.button_element import Button
from framework.container_element import Container
from framework.text_field_element import TextField
from forms_pages.left_menu_form import LeftMenuForm
from data_test import TestData


class WebTablesPage(BasePage):
    __ADD_BTN = ("//*[@id='addNewRecordButton']", "Add button")
    __REGISTRATION_FORM = ("//*[contains(@class,'modal-content')]", "Registration form")
    __FIRST_NAME_INPUT = ("//*[@id='firstName']", "First name input")
    __LAST_NAME_INPUT = ("//*[@id='lastName']", "Last name input")
    __EMAIL_INPUT = ("//*[@id='userEmail']", "Email input")
    __AGE_INPUT = ("//*[@id='age']", "Age input")
    __SALARY_INPUT = ("//*[@id='salary']", "Salary input")
    __DEPARTAMENT_INPUT = ("//*[@id='department']", "Department input")
    __SUBMIT_BTN = ("//*[@id='submit']", "Submit button")
    __HTML_BODY = ("//body", "Body html element")
    __TABLE_CELL = ("//*[contains(@class,'rt-td')]", "Table cell")
    __DELETE_BNT = (
        "//*[contains(@class,'action-buttons')]//*[contains(@title,'Delete')]",
        "Delete btn user1",
    )

    __left_menu = LeftMenuForm()

    @property
    def left_menu(self):
        return self.__left_menu

    def __init__(self):
        super().__init__(
            "//*[contains(@class,'web-tables-wrapper')]", "Web tables form"
        )

    def click_add_btn(self):
        Button(*self.__ADD_BTN).click_element()

    def is_displayed_registration_form(self):
        return Container(*self.__REGISTRATION_FORM).is_displayed()

    def wait_visibility_registration_form(self):
        Container(*self.__REGISTRATION_FORM).wait_visibility_element()

    def send_first_name(self, text):
        TextField(*self.__FIRST_NAME_INPUT).send_keys_input(text)

    def send_last_name(self, text):
        TextField(*self.__LAST_NAME_INPUT).send_keys_input(text)

    def send_email_name(self, text):
        TextField(*self.__EMAIL_INPUT).send_keys_input(text)

    def send_age(self, text):
        TextField(*self.__AGE_INPUT).send_keys_input(text)

    def send_salary(self, text):
        TextField(*self.__SALARY_INPUT).send_keys_input(text)

    def send_departament(self, text):
        TextField(*self.__DEPARTAMENT_INPUT).send_keys_input(text)

    def submit_registration_form(self):
        Button(*self.__SUBMIT_BTN).submit_element()

    def wait_invisibility_registration_form(self):
        Container(*self.__REGISTRATION_FORM).wait_invisibility_element()

    def get_attribute_class_body(self):
        return Container(*self.__HTML_BODY).get_attribute(TestData.ATTRIBUTE)

    def getting_text_table_cell(self):
        return Container(*self.__TABLE_CELL).getting_list_text_elements()

    def find_elements_delete_btn(self):
        return Button(*self.__DELETE_BNT).find_elements()

    def click_delete_latest_str(self):
        self.find_elements_delete_btn()[-1].click()

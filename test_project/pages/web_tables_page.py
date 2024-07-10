from framework.base_page.base_page import BasePage
from framework.elements.button import Button
from framework.elements.text_box import TextBox
from framework.elements.text_field import TextField
from test_project.forms.left_menu_form import LeftMenuForm
from test_project.data.data_test import TestData


class WebTablesPage(BasePage):
    __ADD_BTN = Button("//*[@id='addNewRecordButton']", "Add button")
    __REGISTRATION_FORM = TextBox("//*[contains(@class,'modal-content')]", "Registration form")
    __FIRST_NAME_INPUT = TextField("//*[@id='firstName']", "First name input")
    __LAST_NAME_INPUT = TextField("//*[@id='lastName']", "Last name input")
    __EMAIL_INPUT = TextField("//*[@id='userEmail']", "Email input")
    __AGE_INPUT = TextField("//*[@id='age']", "Age input")
    __SALARY_INPUT = TextField("//*[@id='salary']", "Salary input")
    __DEPARTAMENT_INPUT = TextField("//*[@id='department']", "Department input")
    __SUBMIT_BTN = Button("//*[@id='submit']", "Submit button")
    __HTML_BODY = TextBox("//body", "Body html element")
    __TABLE_CELL = TextBox("//*[contains(@class,'rt-td')]", "Table cell")
    __DELETE_BNT = Button("//*[contains(@class,'action-buttons')]//*[contains(@title,'Delete')]", "Delete btn user1")
    __UNIQ_ELEM_LOCATOR = "//*[contains(@class,'web-tables-wrapper')]"

    __left_menu = LeftMenuForm()

    @property
    def left_menu(self):
        return self.__left_menu

    def __init__(self):
        super().__init__(self.__UNIQ_ELEM_LOCATOR, "Web tables form")

    def click_add_btn(self):
        self.__ADD_BTN.click_element()

    def is_displayed_registration_form(self):
        return self.__REGISTRATION_FORM.is_displayed()

    def wait_visibility_registration_form(self):
        self.__REGISTRATION_FORM.wait_visibility_element()

    def send_all_form(self, first_name, last_name, email, age, salary, departament):
        self.__FIRST_NAME_INPUT.send_keys_input(first_name)
        self.__LAST_NAME_INPUT.send_keys_input(last_name)
        self.__EMAIL_INPUT.send_keys_input(email)
        self.__AGE_INPUT.send_keys_input(age)
        self.__SALARY_INPUT.send_keys_input(salary)
        self.__DEPARTAMENT_INPUT.send_keys_input(departament)

    def submit_registration_form(self):
        self.__SUBMIT_BTN.submit_element()

    def wait_invisibility_registration_form(self):
        self.__REGISTRATION_FORM.wait_invisibility_element()

    def get_attribute_class_body(self):
        return self.__HTML_BODY.get_attribute(TestData.ATTRIBUTE)

    def getting_text_table_cell(self):
        return self.__TABLE_CELL.getting_list_text_elements()

    def find_elements_delete_btn(self):
        return self.__DELETE_BNT.find_elements()

    def click_delete_latest_str(self):
        self.find_elements_delete_btn()[-1].click()

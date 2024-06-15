from .base_page import BasePage
from framework.button_element import ButtonElement
from framework.container_element import ContainerElement
from framework.input_element import InputElement
from forms_pages.left_menu_form import LeftMenuForm


class WebTablesPage(BasePage):
    def __init__(self):
        super().__init__(
            "//*[contains(@class,'web-tables-wrapper')]", "Web tables form"
        )

    left_menu = LeftMenuForm()

    __Add_btn = ButtonElement("//*[@id='addNewRecordButton']", "Add button")
    __Registration_form = ContainerElement(
        "//*[contains(@class,'modal-content')]", "Registration form"
    )
    __First_name_input = InputElement("//*[@id='firstName']", "First name input")
    __Last_name_input = InputElement("//*[@id='lastName']", "Last name input")
    __Email_input = InputElement("//*[@id='userEmail']", "Email input")
    __Age_input = InputElement("//*[@id='age']", "Age input")
    __Salary_input = InputElement("//*[@id='salary']", "Salary input")
    __Departament_input = InputElement("//*[@id='department']", "Department input")
    __Submit_btn = ButtonElement("//*[@id='submit']", "Submit button")
    __Html_body = ContainerElement("//body", "Body html element")
    __Table_cell = ContainerElement("//*[contains(@class,'rt-td')]", "Table cell")
    __Delete_bnt = ButtonElement(
        f"//*[contains(@class,'action-buttons')]//*[contains(@title,'Delete')]",
        "Delete btn user1",
    )

    def click_add_btn(self):
        self.__Add_btn.click_element()

    def is_displayed_registration_form(self):
        return self.__Registration_form.is_displayed()

    def wait_visibility_registration_form(self):
        self.__Registration_form.wait_visibility_element()

    def send_first_name(self, text):
        self.__First_name_input.send_keys_input(text)

    def send_last_name(self, text):
        self.__Last_name_input.send_keys_input(text)

    def send_email_name(self, text):
        self.__Email_input.send_keys_input(text)

    def send_age(self, text):
        self.__Age_input.send_keys_input(text)

    def send_salary(self, text):
        self.__Salary_input.send_keys_input(text)

    def send_departament(self, text):
        self.__Departament_input.send_keys_input(text)

    def submit_registration_form(self):
        self.__Submit_btn.submit_element()

    def wait_invisibility_registration_form(self):
        self.__Registration_form.wait_invisibility_element()

    def get_attribute_class_body(self):
        return self.__Html_body.get_attribute("class")

    def getting_text_table_cell(self):
        return self.__Table_cell.getting_list_text_elements()

    def find_elements_delete_btn(self):
        return self.__Delete_bnt.find_elements()

    def click_delete_latest_str(self):
        self.find_elements_delete_btn()[-1].click()

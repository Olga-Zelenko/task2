class TestData:
    MESSAGE_BUTTON = "You clicked a button"
    MESSAGE_CONFIRM_BOX = "Do you confirm action?"
    MESSAGE_ALERT = "You selected Ok"
    MESSAGE_PROMPT_BOX = "Please enter your name"
    MESSAGE_SEND_KEYS_ALERT = "You entered "
    TEXT_IFRAME1_PARENT = "Parent frame"
    TEXT_IFRAME_CHILD = "Child Iframe"
    CLASS_OPEN_REGISTRATION_FORM = "modal-open"
    URL_SAMPLE = "/sample"

    class User:
        def __init__(self, first_name, last_name, email, age, salary, departament):
            self.first_name = first_name
            self.last_name = last_name
            self.email = email
            self.age = age
            self.salary = salary
            self.departament = departament


user_1 = TestData.User("Jon", "Snow", "knownothing@gmail.com", 30, 3000, "alpha")
user_2 = TestData.User("Buttercup", "Cumbercnatch", "BudapestCandygram@mail.ru", 41, 2000, "beta")


from models.user_class import User


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
    ATTRIBUTE = "class"
    NUMBER_FRAMES = 1


user_1 = User("Jon", "Snow", "knownothing@gmail.com", 30, 3000, "alpha")
user_2 = User(
    "Buttercup", "Cumbercnatch", "BudapestCandygram@mail.ru", 41, 2000, "beta"
)

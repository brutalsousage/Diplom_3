from selenium.webdriver.common.by import By

class LoginPageLocators:
    PASSWORD_INPUT = (By.XPATH, "//input[@type='password']")
    LOGIN_BUTTON = (By.XPATH, "//button[contains(text(), 'Войти')]")
    EMAIL_INPUT = (By.XPATH, "//input[@name='name' or @type='email']")

from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
class LoginPageLocators():
    LOGIN_EMAIL = (By.CSS_SELECTOR, "#id_login-username")
    LOGIN_PASSWORD = (By.CSS_SELECTOR, "#id_login-password")
    LOGIN_REGISTR_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    LOGIN_REGISTR_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
    LOGIN_REGISTR_REPASSWORD = (By.CSS_SELECTOR, "#id_registration-password2")
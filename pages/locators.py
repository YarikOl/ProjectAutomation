from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
class LoginPageLocators():
    LOGIN_EMAIL = (By.CSS_SELECTOR, "#id_login-username")
    LOGIN_PASSWORD = (By.CSS_SELECTOR, "#id_login-password")
    LOGIN_REGISTR_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    LOGIN_REGISTR_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
    LOGIN_REGISTR_REPASSWORD = (By.CSS_SELECTOR, "#id_registration-password2")
class ProductPageLocators():
    ADD_TO_CART = (By.XPATH, "/html/body/div[2]/div/div[2]/div[2]/article/div/div[2]/form/button")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div[class='container-fluid page'] div:nth-child(2) div:nth-child(1) strong:nth-child(1)")
class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_to_cart(self):
        link = self.browser.find_element(*ProductPageLocators.ADD_TO_CART)
        link.click()
    def product_name_should_be_right(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME), "Login link is not presented"
        assert 'Coders at Work' == self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text, "Not right product name"

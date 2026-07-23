from selenium.webdriver.common.by import By
from utils.waits import *
from pages.base_page import BasePage

class CartPage(BasePage):
    """Page object for managing shopping cart"""
    cart_icon = (By.CLASS_NAME, "shopping_cart_link")
    add_to_cart_btn = (By.CSS_SELECTOR, "button[id^='add-to-cart']")
    remove_from_cart_btn = (By.CSS_SELECTOR, "button[id^='remove']")
    cart_badge = (By.CLASS_NAME, "shopping_cart_badge")

    def __init__(self, driver):
        super().__init__(driver)

    def add_product(self):
        """Clicks 'Add to Cart' button"""
        self.click(self.add_to_cart_btn)

    def remove_product(self):
        """Clicks 'Remove from Cart' button"""
        self.click(self.remove_from_cart_btn)

    def go_to_cart(self):
        """Navigates the cart page by clicking the shopping cart icon"""
        self.click(self.cart_icon)

    def get_cart_count(self):
        """Returns the current number of items displayed on the cart badge as an integer"""
        if self.is_displayed(self.cart_badge):
            return int(self.get_text(self.cart_badge))
        return 0

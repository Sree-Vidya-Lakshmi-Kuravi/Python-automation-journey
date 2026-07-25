from selenium.webdriver.common.by import By
from utils.waits import *
from pages.base_page import BasePage


class InventoryPage(BasePage):
    """Page Object for Inventory"""
    url = "https://www.saucedemo.com/inventory.html"

    title_header = (By.CLASS_NAME, "title")
    product_items = (By.CLASS_NAME, "inventory_item")
    product_names = (By.CLASS_NAME, "inventory_item_name")

    def __init__(self, driver):
        super().__init__(driver)

    def is_inventory_loaded(self):
        """Checks if inventory page header is loaded and URL matches"""
        return self.is_displayed(self.title_header) and self.url in self.driver.current_url

    def get_product_count(self):
        """Returns the total length of products"""
        products = self.wait.wait_for_eles_visibility(self.product_items)
        return len(products)

    def get_product_names(self):
        """Returns the names of products"""
        names = self.wait.wait_for_eles_visibility(self.product_names)
        name_list = [n.text for n in names]
        return name_list

    
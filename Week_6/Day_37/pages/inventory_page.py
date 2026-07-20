from selenium.webdriver.common.by import By
from utils.waits import WaitUtils

class InventoryPage:
    url = "https://www.saucedemo.com/inventory.html"

    title_header = (By.CLASS_NAME, "title")
    product_items = (By.CLASS_NAME, "inventory_item")
    product_names = (By.CLASS_NAME, "inventory_item_name")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WaitUtils(self.driver, timeout = 10)

    def is_inventory_loaded(self):
        title = self.wait.wait_for_visibility(self.title_header)

        if "inventory.html" in self.driver.current_url:
            return True
        else:
            return False

    def get_product_count(self):
        products = self.wait.wait_for_eles_visibility(self.product_items)
        return len(products)

    def get_product_names(self):
        names = self.wait.wait_for_eles_visibility(self.product_names)
        name_list = [n.text for n in names]
        return name_list

    
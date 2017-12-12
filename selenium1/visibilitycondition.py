from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import unittest

class ExplictWaitTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("http://demo-store.seleniumacademy.com")

    def test_create_new_customer(self):
        self.driver.find_element_by_link_text("ACCOUNT").click()
        my_account = WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located((By.LINK_TEXT,"My Account")))
        my_account.click()
        create_account_button = WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.LINK_TEXT,"CREATE AN ACCOUNT")))
        create_account_button.click()
        WebDriverWait(self.driver, 10).until(expected_conditions.title_contains(("Create New Customer Account")))

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
        unittest.main(verbosity=2)
        
                                                          
                                                          

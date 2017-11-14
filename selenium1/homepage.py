import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

class HomepageTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(30)
        cls.driver.maximize_window()
        cls.driver.get('http://demo-store.seleniumacademy.com')

    def test_search_field(self):
        self.assertTrue(self.is_element_present(By.NAME,'q'))

    def test_language_option(self):
        self.assertTrue(self.is_element_present(By.ID,'select-language'))

    def test_shopping_cart_empty_message(self):
        shopping_cart_icon = self.driver.find_element_by_css_selector('div.header-minicart span.icon')
        shopping_cart_icon.click()
        shopping_cart_status = self.driver.find_element_by_css_selector('p.empty').text
        self.assertEqual('You have no items in your shopping cart.',shopping_cart_status)
        close_button = self.driver.find_element_by_css_selector('div.minicart-wrapper a.close')
        close_button.click()


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def is_element_present(self,how,what):
        try:
            self.driver.find_element(by=how,value= what)
        except NOSuchElementException:
            return False
        return True

    
if __name__ == '__main__':
    unittest.main(verbosity=2)

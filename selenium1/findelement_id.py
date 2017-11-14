import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

class SearchTests(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.driver.get('http://demo-store.seleniumacademy.com')

    def test_search_text_field_max_length(self):
        self.search_field = self.driver.find_element_by_id("search")
        self.assertEqual("178",self.search_field.get_attribute("maxlength"))

    
    def tearDown(self):
        self.driver.quit()
if __name__ == '__main__':
    unittest.main(verbosity=2)

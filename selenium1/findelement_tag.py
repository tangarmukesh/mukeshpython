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
        
    def test_count_of_promo_banners_images(self):
        #banner_list = self.driver.find_element_by_class_name("promos")
        #banners = banner_list.find_elements_by_tag_name("img")
        banners = self.driver.find_elements_by_tag_name("img")
        self.assertEqual(3, len(banners))

    def tearDown(self):
        self.driver.quit()
    
if __name__ == '__main__':
    unittest.main(verbosity=2)

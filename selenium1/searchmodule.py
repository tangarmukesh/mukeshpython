import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

'''class SearchTests(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.driver.get('http://demo-store.seleniumacademy.com')

    def test_search_by_category(self):
        self.search_field = self.driver.find_element_by_name('q')
        self.search_field.clear()
        self.search_field.send_keys('phones')
        self.search_field.submit()
        product = self.driver.find_elements_by_xpath("//h2[@class= 'product-name']/a")
        #self.assertEqual(2,len(product))
        self.assertEqual(3,len(product))

    def test_search_by_name(self):
        self.search_field = self.driver.find_element_by_name('q')
        self.search_field.clear()
        self.search_field.send_keys('salt shaker')
        self.search_field.submit()
        product = self.driver.find_elements_by_xpath("//h2[@class= 'product-name']/a")
        #self.assertEqual(2,len(product))
        self.assertEqual(1,len(product))

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)'''

class SearchTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(30)
        cls.driver.maximize_window()
        cls.driver.get('http://demo-store.seleniumacademy.com')

    def test_search_by_category(self):
        self.search_field = self.driver.find_element_by_name('q')
        self.search_field.clear()
        self.search_field.send_keys('phones')
        self.search_field.submit()
        product = self.driver.find_elements_by_xpath("//h2[@class= 'product-name']/a")
        #self.assertEqual(2,len(product))
        self.assertEqual(3,len(product))

    def test_search_by_name(self):
        self.search_field = self.driver.find_element_by_name('q')
        self.search_field.clear()
        self.search_field.send_keys('salt shaker')
        self.search_field.submit()
        product = self.driver.find_elements_by_xpath("//h2[@class= 'product-name']/a")
        #self.assertEqual(2,len(product))
        self.assertEqual(1,len(product))

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)















        

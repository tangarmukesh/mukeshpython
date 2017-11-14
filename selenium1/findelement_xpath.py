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
        
    def test_xpath(self):
        women= self.driver.find_element_by_xpath("/html/body/div/div[2]/header/div/div[3]/nav/ol/li[1]/a")

    def tearDown(self):
        self.driver.quit()
    
if __name__ == '__main__':
    unittest.main(verbosity=2)'''


class SearchTests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.driver.get('http://demo-store.seleniumacademy.com')
        
    def test_xpath(self):
        #women= self.driver.find_element_by_xpath('//*[@id="nav"]/ol/li[1]/a')
        #women= self.driver.find_element_by_xpath('//input')
        women= self.driver.find_element_by_xpath('//input[2]')
        self.assertEqual('128',women.get_attribute('maxlength'))
        

    def tearDown(self):
        self.driver.quit()
    
if __name__ == '__main__':
    unittest.main(verbosity=2)


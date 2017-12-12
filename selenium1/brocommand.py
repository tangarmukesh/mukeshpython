from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import unittest

class NavigationTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(1)
        self.driver.maximize_window()
        #self.driver.get("http://demo-store.seleniumacademy.com")
        self.driver.get("http://www.google.com")

    def testBrowserNavigation(self):
        driver = self.driver
        search_field = driver.find_element_by_name("q")
        search_field.send_keys("selenium webdriver")
        search_field.submit()
        se_wd_link = driver.find_element_by_link_text("Selenium WebDriver")
        se_wd_link.click()
        self.assertEqual("Selenium WebDriver",driver.title)
        driver.back()
        self.assertTrue(WebDriverWait(self.driver, 10).until(expected_conditions.title_is("selenium webdriver - Google Search" )))
        driver.forward()
        self.assertTrue(WebDriverWait(self.driver, 10).until(expected_conditions.title_is("Selenium WebDriver")))
        driver.refresh()
        self.assertTrue(WebDriverWait(self.driver, 10).until(expected_conditions.title_is("Selenium WebDriver")))

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
        unittest.main(verbosity=2)
        





    

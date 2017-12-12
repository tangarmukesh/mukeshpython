from selenium import webdriver
import unittest

class CompareProduects(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.driver.get("http://demo-store.seleniumacademy.com")

    def test_compare_produects_removal_alert(self):
        search_field = self.driver.find_element_by_name("q")
        search_field.clear()
        search_field.send_keys("phones")
        search_field.submit()
        self.driver.find_element_by_link_text("Add to Compare").click()
        self.driver.find_element_by_link_text("Clear All").click()
        # switch to alert
        alert = self.driver.switch_to_alert()
        alert_text = alert.text
        self.assertEqual("Are you sure you would like to remove all products from your comparison?",alert_text)
        alert.accept()

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
        unittest.main(verbosity=2)

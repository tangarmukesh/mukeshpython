from selenium import webdriver
from selenium.webdriver.support.ui import Select
from time import gmtime, strftime
import unittest
class RegisterNewUser(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(0)
        self.driver.maximize_window()
        self.driver.get("http://demo-store.seleniumacademy.com")

    def test_language_options(self):
        exp_options = ["English", "French", "German"]
        act_options = []
        select_language = Select(self.driver.find_element_by_id("select-language"))
        self.assertEqual(3, len(select_language.options))
        for options in select_language.options:
            act_options.append(options.text)
        self.assertListEqual(exp_options, act_options)
        self.assertEqual("English", select_language.first_selected_option.text)
        select_language.select_by_visible_text("German")
        self.assertTrue("store=german" in self.driver.current_url)
        select_language = Select(self.driver.find_element_by_id("select-language"))
        select_language.select_by_index(0)


if __name__ == "__main__":
        unittest.main(verbosity=2)

    

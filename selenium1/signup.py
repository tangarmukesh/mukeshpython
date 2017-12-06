from selenium import webdriver
from time import gmtime, strftime
import unittest
class RegisterNewUser(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.driver.get("http://demo-store.seleniumacademy.com")

    def test_register_new_user(self):
        driver = self.driver
        driver.find_element_by_link_text("ACCOUNT").click()
        driver.find_element_by_link_text("My Account").click()

        create_account_button= driver.find_element_by_xpath("//a[@title='Create an Account']")
        create= self.assertTrue(create_account_button.is_displayed() and create_account_button.is_enabled())
        print(create)
        create_account_button.click()
        self.assertEqual("Create New Customer Account",driver.title)
        first_name = driver.find_element_by_id("firstname")
        last_name = driver.find_element_by_id("lastname")
        email_address = driver.find_element_by_id("email_address")
        news_letter_subscription = driver.find_element_by_id("is_subscribed")
        password = driver.find_element_by_id("password")
        confirm_password = driver.find_element_by_id("confirmation")
        submit_button = driver.find_element_by_xpath("//button[@title= 'Register']")
        self.assertEqual("255",first_name.get_attribute("maxlength"))
        self.assertEqual("255",last_name.get_attribute("maxlength"))
        self.assertTrue(first_name.is_enabled()
                        and last_name.is_enabled()
                        and email_address.is_enabled()
                        and news_letter_subscription.is_enabled()
                        and password.is_enabled()
                        and confirm_password.is_enabled()
                        and submit_button.is_enabled())
        self.assertFalse(news_letter_subscription.is_selected())
        user_name = "user_" + strftime("%y%m%d%H%M%S",gmtime())
        firstname = "Mukesh"
        first_name.send_keys(firstname)
        last_name.send_keys(user_name)
        email_address.send_keys(user_name+"@gmail.com")
        news_letter_subscription.click()
        password.send_keys("12345678")
        confirm_password.send_keys("12345678")
        submit_button.click()
        self.assertEqual("Hello, " + firstname +" "+ user_name + "!",driver.find_element_by_css_selector("p.hello > strong").text)
        driver.find_element_by_link_text("ACCOUNT").click()
        self.assertTrue(driver.find_element_by_link_text("Log Out").is_displayed())
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
        unittest.main(verbosity=2)
    
    
        

        

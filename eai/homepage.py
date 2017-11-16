import unittest
from selenium.webdriver.common.action_chains import ActionChains
from eai.pagelib.Homepage import *
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.implicitly_wait(30)
driver.maximize_window()
driver.get('http://staging.engineer.ai/home')
'''
#Open inter_chat
driver.switch_to_frame(driver.find_element_by_name("intercom-launcher-discovery-frame"))
time.sleep(5)
chat_open = driver.find_element_by_xpath("//img").click()

#Close inter_chat
#chat_close = driver.find_element_by_id("intercom-launcher").click()

chat_open = driver.find_element_by_xpath("//img").click()

driver.switch_to_default_content()'''

#Select app type

#select_app_type('Web',driver)
mobile_app = driver.find_element_by_id('top_card_0')
mobile_app.click()

#selct templates
#cloud_management = driver.find_element_by_xpath("//h3[text()='Cloud Management']")
#cloud_management.click()
uber_temp = driver.find_element_by_xpath("//h3[text()='Uber']")
uber_temp.click()

#ola_temp = driver.find_element_by_xpath("//h3[text()='Ola']")
#ola_temp.click()

#Slack_temp = driver.find_element_by_xpath("//h3[text()='Slack']")
#Slack_temp.click()


#Click on Next button

next_button = driver.find_element_by_xpath("//button[@class='next']")
next_button.click()

#Check platforms

check_platform = driver.find_elements_by_xpath("//div[@class='platformDrag']/ul/li")
print('Found' + str(len(check_platform)) + 'platforms')

#select platforms

time.sleep(10);
spec_button = driver.find_element_by_xpath("//button[@class='addSpec']")
spec_button.click()
macos_platform = driver.find_element_by_xpath("//h3[text()='macOS']")
driver.execute_script("arguments[0].scrollIntoView();", macos_platform)
macos_platform.click()
#next_button = driver.find_element_by_xpath("//div[@class='platformRight']//button[@class='next']")
next_button = driver.find_element_by_xpath("//button[@class='next']")
#button = next_button.get_attribute("class")
#print(button)
next_button.click()

#Feature

next_button = driver.find_element_by_xpath("(//div[@class='featureRight']/button)[2]")
next_button.click()

#Team and Speed

time.sleep(5);
#next_button = driver.find_element_by_xpath("//teamspeedcard/div[@class='timeBottomBar active']/div/div[@class='timeRight']/button")
next_button = driver.find_element_by_xpath("//div[@class='timeRight']/button")
next_button.click()

#Phases

#support_phase = driver.find_element_by_xpath("//div[@class='fancyCheck']/label")
#driver.execute_script("arguments[0].scrollIntoView();", support_phase)
#support_phase.click()
next_button = driver.find_element_by_xpath("//div[@class='phasesRight']/button")
next_button.click()

#SignIn
user_mail = driver.find_element_by_name("email").send_keys("mukeshtangar@gmail.com")
user_password = driver.find_element_by_name("password").send_keys("12345678")
signin_button = driver.find_element_by_class_name("submitButton").click()

#Closs NDA popup
nda_later = driver.find_element_by_class_name("doLater").click()

#Goto dashboard
user_dashboard = driver.find_element_by_class_name("betterQuote").click()

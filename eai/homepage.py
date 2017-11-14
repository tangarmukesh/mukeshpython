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
chat_open = driver.find_element_by_xpath("//*[@id='intercom-container']/div/div[2]")
chat_open.click()

#Close inter_chat
chat_close = driver.find_element_by_xpath("//*[@id='intercom-container']/div/div[2]")
chat_close.click()
'''

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

'''macos_platform = driver.find_element_by_xpath("//h3[text()='macOS']")
driver.execute_script("arguments[0].scrollIntoView();", macos_platform)
macos_platform.click()'''


#spec_button = driver.find_element_by_xpath("//button[@class='addSpec']")
#spec_button.click()

#WebDriverWait wait = new WebDriverWait(driver);

time.sleep(10);
next_button = driver.find_element_by_xpath("//div[@class='platformRight']//button[@class='next']")
button = next_button.get_attribute("class")
print(button)
next_button.click()
#webdriver.ActionChains(driver).move_to_element(next_button).click().perform()

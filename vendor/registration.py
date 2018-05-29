from selenium import webdriver
from time import gmtime, strftime
import unittest
driver = webdriver.Chrome()
driver.implicitly_wait(30)
driver.maximize_window()
driver.get("https://staging-partner.engineer.ai/register")



import unittest
from selenium import webdriver
'''class SearchTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.driver.get('http://demo-store.seleniumacademy.com')'''

driver = webdriver.Chrome()
driver.implicitly_wait(30)
driver.maximize_window()
driver.get('http://demo-store.seleniumacademy.com')

#Test Search testbox
search_test = driver.find_element_by_name('q')
search_test.clear()

#Enter search keyword
search_test.send_keys('phones')
search_test.submit()

#find elements by xpath
products = driver.find_elements_by_xpath("//h2[@class= 'product-name']/a")
print('Found'+str(len(products))+ 'products')
for product in products:
    print(product.text)
driver.quit()

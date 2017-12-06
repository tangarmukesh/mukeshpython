from selenium import webdriver

def select_app_type(apptype, webdriver):
    webdriver.find_element_by_xpath("//basecard//div[text()='%s']//following-sibling::div//div[@class='clickTwo']" % apptype).click()




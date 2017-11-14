from selenium import webdriver

def select_app_type(apptype, webdriver):
    webdriver.find_element_by_xpath("//basecard//div[text()='%s']//following-sibling::div//div[@class='clickTwo']" % apptype).click()



def inter_chat():
    #webdriver.find_element_by_xpath("//div[@class='intercom-borderless-dismiss-button']").click()
    #inter_popup = webdriver.find_element_by_xpath("//div[@class='intercom-borderless-body']")
    inter_chat = webdriver.find_element_by_xpath("//div[@class='intercom-borderless-dismiss-button']")
    #actions = inter_chat(webdriver)
    #actions.move_to_element(inter_chat).click().perform()
    webdriver.ActionChains(webdriver).move_to_element(inter_chat).click().perform()

from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
browser=webdriver.Firefox(executable_path="E:\geckodriver-v0.29.1-win64\geckodriver")
browser.get("http://mobile.pinduoduo.com/")
sleep(2)
browser.refresh()
element=browser.find_element_by_class_name("_2bfwu6WT").click()
search_key="菠萝"

#ActionChains(browser).move_to_element(element).perform()


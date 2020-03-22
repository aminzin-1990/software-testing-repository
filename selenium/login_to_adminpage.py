from selenium import webdriver
import time


link = " http://localhost/litecart/admin/"

browser = webdriver.Chrome()

try:
    browser.get(link)

    login = browser.find_element_by_css_selector("[name='username']")
    login.send_keys("admin")

    password = browser.find_element_by_css_selector("[name='password']")
    password.send_keys("admin")

    button = browser.find_element_by_css_selector("[name='login']")
    button.click()
finally:
    time.sleep(3)
    browser.quit()

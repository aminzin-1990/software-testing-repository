from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from time import time
import os


url = 'http://localhost/litecart/admin'
browser = webdriver.Chrome()
browser.implicitly_wait(3)
browser.get(url)



def authorization_to_admin_page(wb, url_link):
    wb.get(url_link)
    login = wb.find_element_by_name("username")
    login.send_keys("admin")

    password = wb.find_element_by_name("password")
    password.send_keys("admin")

    button = wb.find_element_by_name("login")
    button.click()


try:
    authorization_to_admin_page(browser, url)
    sleep(1)
    browser.find_element_by_link_text("Catalog").click()
    browser.find_element_by_link_text("Add New Product").click()
    # General
    sleep(1)
    browser.find_element_by_css_selector("[name='status'][value='1']").click()
    name_new_product = browser.find_element_by_name("name[en]")
    name_new_product.send_keys("Hulk")
    code_new_product = browser.find_element_by_name("code")
    code_new_product.send_keys("111")
    quantity_new_product = browser.find_element_by_name("quantity")
    quantity_new_product.clear()
    quantity_new_product.send_keys("10")
    image_new_product = browser.find_element_by_name("new_images[]")
    path_directory = os.getcwd()
    name_of_your_file = 'hulk.jpg'
    path_image = os.path.join(path_directory, name_of_your_file)
    image_new_product.send_keys(path_image)
    browser.find_element_by_name('date_valid_from').click()
    browser.find_element_by_name('date_valid_from').send_keys('10-04-2020')
    browser.find_element_by_name('date_valid_to').click()
    browser.find_element_by_name('date_valid_to').send_keys('20-04-2020')

    # Information
    browser.find_element_by_link_text("Information").click()
    sleep(1)
    browser.find_element_by_xpath(
        "//div[@id='tab-information']//select[normalize-space(.)='-- Select -- ACME Corp.']//option[2]").click()
    keywords_new_product = browser.find_element_by_name("keywords")
    keywords_new_product.send_keys("hulk")
    short_desc_new_product = browser.find_element_by_name("short_description[en]")
    short_desc_new_product.send_keys("Superhero of the Marvel")
    desc_new_product = browser.find_element_by_class_name("trumbowyg-editor")
    desc_new_product.send_keys("BIG GREEN STRONG MAN")
    title_new_product = browser.find_element_by_name("head_title[en]")
    title_new_product.send_keys("Superhero")
    # Price
    browser.find_element_by_link_text("Prices").click()
    sleep(1)
    price = browser.find_element_by_name("purchase_price")
    price.clear()
    price.send_keys("300")
    browser.find_element_by_xpath("//div[@id='tab-prices']/table[1]/tbody/tr/td/select//option[3]").click()

    button_save = browser.find_element_by_name("save")
    button_save.click()
    sleep(1)
    assert browser.find_element_by_link_text("Hulk"), "Product is not created"
finally:
    browser.quit()

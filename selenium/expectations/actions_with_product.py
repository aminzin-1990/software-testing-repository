from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from random import randint
from time import sleep


url = "http://localhost/litecart/en/"
browser = webdriver.Chrome()

try:
    browser.get(url)

    for i in range(3):
        ducks = browser.find_elements_by_css_selector(".products li")
        ducks[randint(0, len(ducks) - 1)].find_element_by_css_selector("a.link").click()

        if browser.find_elements_by_css_selector("#box-product .sale"):
            browser.find_element_by_tag_name("select").send_keys('Small')
        browser.find_element_by_css_selector(".quantity [name='add_cart_product']").click()
        sleep(1)
        alert = browser.switch_to.alert
        alert.accept()
        wait = WebDriverWait(browser, 10)
        element = wait.until(
            ec.text_to_be_present_in_element((By.XPATH, ".//*[ @ id = 'cart']//a//span[@class='quantity']"), str(i)))
        browser.get(url)

    browser.get("http://localhost/litecart/en/checkout")
    count_in_basket = browser.find_elements_by_css_selector(
        "#order_confirmation-wrapper .rounded-corners tbody tr:not(.header) .item")
    for i in range(len(count_in_basket)):
        browser.find_element_by_name('remove_cart_item').click()

        wait = WebDriverWait(browser, 10)
        wait.until(ec.staleness_of(count_in_basket[0]))
finally:
    browser.quit()

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from time import time


url = 'http://localhost/litecart/en/'
browser = webdriver.Chrome()

browser.get(url)

email_address = str(time()) + "@email.org"
password_text = str(time()) + "password"

try:
    browser.implicitly_wait(5)

    button_create_new_acc = browser.find_element_by_css_selector("#box-account-login .content tr td a")
    button_create_new_acc.click()

    sleep(1)

    first_name = browser.find_element_by_css_selector("[name='firstname']")
    first_name.send_keys('first')

    last_name = browser.find_element_by_css_selector("[name='lastname']")
    last_name.send_keys('last')

    address_1 = browser.find_element_by_css_selector("[name='address1']")
    address_1.send_keys('address1')

    postcode = browser.find_element_by_css_selector("[name='postcode']")
    postcode.send_keys('11111')

    city = browser.find_element_by_css_selector("[name='city']")
    city.send_keys('Washington')

    phone = browser.find_element_by_css_selector("[name='phone']")
    phone.send_keys('1-111-111-1111')

    country = browser.find_element_by_css_selector(".select2-selection__rendered")
    country.click()

    country_input = browser.find_element_by_css_selector(".select2-search__field")
    country_input.send_keys('United States')
    country_input.send_keys(Keys.ENTER)

    email_registration_page = browser.find_element_by_css_selector("[name='email']")
    email_registration_page.send_keys(email_address)

    password_registration_page = browser.find_element_by_css_selector("[name='password']")
    password_registration_page.send_keys(password_text)

    confirmed_password = browser.find_element_by_css_selector("[name='confirmed_password']")
    confirmed_password.send_keys(password_text)

    create_button = browser.find_element_by_css_selector("[name='create_account']")
    create_button.click()

    password_registration_page = browser.find_element_by_css_selector("[name='password']")
    password_registration_page.send_keys(password_text)

    confirmed_password = browser.find_element_by_css_selector("[name='confirmed_password']")
    confirmed_password.send_keys(password_text)

    create_button = browser.find_element_by_css_selector("[name='create_account']")
    create_button.click()

    sleep(1)

    logout = browser.find_element_by_link_text('Logout')
    logout.click()

    sleep(1)

    email_main_page = browser.find_element_by_css_selector("[name='email']")
    email_main_page.send_keys(email_address)

    password_main_page = browser.find_element_by_css_selector("[name='password']")
    password_main_page.send_keys(password_text)

    login = browser.find_element_by_css_selector("[name='login']")
    login.click()

    sleep(1)

    logout = browser.find_element_by_link_text('Logout')
    logout.click()
finally:
    browser.quit()

from selenium import webdriver
from time import sleep

url = "http://localhost/litecart/admin/?app=catalog&doc=catalog&category_id=1"

browser = webdriver.Chrome()
browser.implicitly_wait(3)
logs = ''

try:
    browser.get(url)

    browser.find_element_by_css_selector("[name='username']").send_keys("admin")
    browser.find_element_by_css_selector("[name='password']").send_keys("admin")
    browser.find_element_by_css_selector("[name='login']").click()

    for i in range(len(browser.find_elements_by_css_selector("table.dataTable [href*='product_id']:not([title])"))):
        products = browser.find_elements_by_css_selector("table.dataTable [href*='product_id']:not([title])")
        sleep(1)
        products[i].click()
        for j in browser.get_log("browser"):
            logs = "\n".join(str(j))
        browser.execute_script("window.history.go(-1)")
        assert logs == '', "Logs are not empty"
finally:
    browser.quit()
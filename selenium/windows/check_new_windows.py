from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as ec


url = "http://localhost/litecart/admin/?app=countries&doc=countries"

browser = webdriver.Chrome()
browser.implicitly_wait(3)


try:
    browser.get(url)
    browser.find_element_by_css_selector("[name='username']").send_keys("admin")
    browser.find_element_by_css_selector("[name='password']").send_keys("admin")
    browser.find_element_by_css_selector("[name='login']").click()

    browser.find_element_by_class_name("button").click()

    main_window = browser.current_window_handle
    test_link_list = browser.find_elements_by_class_name("fa-external-link")
    wait = WebDriverWait(browser, 5)
    for i in test_link_list:
        i.click()
        new_window = [i for i in browser.window_handles if i != main_window]
        # wait.until(ec.new_window_is_opened(new_window))
        browser.switch_to.window(new_window[0])
        browser.close()
        browser.switch_to.window(main_window)
finally:
    browser.quit()

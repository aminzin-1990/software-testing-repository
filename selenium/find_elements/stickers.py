from selenium import webdriver

url = "http://localhost/litecart/en/"

browser = webdriver.Chrome()
browser.implicitly_wait(2)

amount_sticker = 0

try:
    browser.get(url)
    ducks = browser.find_elements_by_css_selector(".products > li")
    amount_ducks = len(browser.find_elements_by_css_selector(".products > li"))
    for i in range(amount_ducks):
        if len(ducks[i].find_elements_by_css_selector(".products > li > .link > .image-wrapper .sticker")) != 1:
            print(i, 'DUCK HAS BUG')
        else:
            amount_sticker += 1
    if amount_ducks == amount_sticker:
        print('NO BUG')
finally:
    browser.quit()

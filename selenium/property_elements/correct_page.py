from selenium import webdriver

link = "http://localhost/litecart/"

browser = webdriver.Chrome()
# browser = webdriver.Firefox()
# browser = webdriver.Ie()


def is_correct_name(bw):
    browser.get("http://localhost/litecart/")
    browser.implicitly_wait(3)
    name_from_main_page = bw.find_element_by_css_selector("#box-campaigns .name").text
    bw.find_element_by_css_selector("#box-campaigns a").click()
    name_from_product_page = bw.find_element_by_css_selector("#box-product h1.title").text
    assert name_from_main_page == name_from_product_page


def is_correct_price_regular(bw):
    browser.get("http://localhost/litecart/")
    browser.implicitly_wait(3)
    price_from_main_page = bw.find_element_by_css_selector("#box-campaigns .regular-price").text
    bw.find_element_by_css_selector("#box-campaigns a").click()
    price_from_product_page = bw.find_element_by_css_selector(".regular-price").text
    assert price_from_main_page == price_from_product_page


def is_correct_price_campaign(bw):
    browser.get("http://localhost/litecart/")
    browser.implicitly_wait(3)
    price_from_main_page = bw.find_element_by_css_selector("#box-campaigns .campaign-price").text
    bw.find_element_by_css_selector("#box-campaigns a").click()
    price_from_product_page = bw.find_element_by_css_selector(".campaign-price").text
    assert price_from_main_page == price_from_product_page


def is_grey_color(bw):
    browser.get("http://localhost/litecart/")
    browser.implicitly_wait(3)
    color_main_page = bw.find_element_by_css_selector("#box-campaigns s.regular-price").value_of_css_property('color')
    rgb_list_main_page = color_main_page[color_main_page.find('(') + 1:color_main_page.find(')')].split(', ')
    bw.find_element_by_css_selector("#box-campaigns a").click()
    color_product_page = bw.find_element_by_css_selector("s.regular-price").value_of_css_property('color')
    rgb_list_product_page = color_main_page[color_product_page.find('(') + 1:color_product_page.find(')')].split(', ')
    assert rgb_list_main_page[0] == rgb_list_main_page[1] == rgb_list_main_page[2]
    assert rgb_list_product_page[0] == rgb_list_product_page[1] == rgb_list_product_page[2]


def is_red_color(bw):
    browser.get("http://localhost/litecart/")
    browser.implicitly_wait(3)
    color_main_page = bw.find_element_by_css_selector("#box-campaigns strong.campaign-price").\
        value_of_css_property('color')
    rgb_list_main_page = color_main_page[color_main_page.find('(') + 1:color_main_page.find(')')].split(', ')
    bw.find_element_by_css_selector("#box-campaigns a").click()
    color_product_page = bw.find_element_by_css_selector("strong.campaign-price").value_of_css_property('color')
    rgb_list_product_page = color_main_page[color_product_page.find('(') + 1:color_product_page.find(')')].split(', ')
    assert rgb_list_main_page[1] == rgb_list_main_page[2] == '0'
    assert rgb_list_product_page[1] == rgb_list_product_page[2] == '0'


def is_font_size(bw):
    browser.get("http://localhost/litecart/")
    browser.implicitly_wait(3)
    regular_size_main_page = bw.find_element_by_css_selector("#box-campaigns s.regular-price").\
        value_of_css_property('font-size')
    campaign_size_main_page = bw.find_element_by_css_selector("#box-campaigns strong.campaign-price").\
        value_of_css_property('font-size')
    bw.find_element_by_css_selector("#box-campaigns a").click()
    regular_size_product_page = bw.find_element_by_css_selector("s.regular-price").\
        value_of_css_property('font-size')
    campaign_size_product_page = bw.find_element_by_css_selector("strong.campaign-price").\
        value_of_css_property('font-size')
    assert regular_size_main_page < campaign_size_main_page
    assert regular_size_product_page < campaign_size_product_page


try:
    # is_correct_name(browser)
    # is_correct_price_regular(browser)
    # is_correct_price_campaign(browser)
    is_grey_color(browser)
    is_red_color(browser)
    # is_font_size(browser)
finally:
    browser.quit()

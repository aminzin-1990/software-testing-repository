from selenium import webdriver

url_step_1 = "http://localhost/litecart/admin/?app=countries&doc=countries"
url_step_2 = "http://localhost/litecart/admin/?app=geo_zones&doc=geo_zones"

browser = webdriver.Chrome()
browser.implicitly_wait(3)


# функция для авторизация под админом
def authorization_to_admin_page(wb, url_link):
    wb.get(url_link)
    login = wb.find_element_by_css_selector("[name='username']")
    login.send_keys("admin")

    password = wb.find_element_by_css_selector("[name='password']")
    password.send_keys("admin")

    button = wb.find_element_by_css_selector("[name='login']")
    button.click()


# функция для проверки отсортированности стран на форме
def countries_sort(wb, url_link):
    authorization_to_admin_page(wb, url_link)

    countries_list = []

    countries_form = browser.find_element_by_css_selector("[name='countries_form']")
    countries_row = countries_form.find_elements_by_css_selector("table > tbody > .row > td:not([style]) a")

    for i in countries_row:
        countries_list.append(i.text)
    sorted_countries_list = sorted(countries_list)

    assert sorted_countries_list == countries_list, 'Countries are not sorted'


# функция для проверки отсортированности зон для стран, в которых они имеются
def country_zones_sort_step_1(wb, url_link):
    authorization_to_admin_page(wb, url_link)

    countries_list_with_zone = []
    count_countries_with_zone = 0
    count_test = 0

    countries_form = browser.find_element_by_css_selector("[name='countries_form']")
    countries_row = countries_form.find_elements_by_css_selector("table > tbody > .row")

    for i in countries_row:
        column = i.find_elements_by_tag_name("td")
        if int(column[5].text) > 1:
            count_countries_with_zone += 1
            country = i.find_element_by_css_selector("td:not([style]) a")
            countries_link = country.get_attribute("href")
            countries_list_with_zone.append(countries_link)

    for i in countries_list_with_zone:
        country_zones_list = []
        browser.get(i)
        zones_form = browser.find_element_by_css_selector(".dataTable tbody")
        zones_row = zones_form.find_elements_by_css_selector("tr")
        for j in zones_row[1:len(zones_row)-1]:
            column = j.find_elements_by_css_selector("td")
            country_zones_list.append(column[2].text)
        sorted_country_zones_list = sorted(country_zones_list)
        if sorted_country_zones_list == country_zones_list:
            count_test += 1

    assert count_test == count_countries_with_zone, 'Zones are not sorted'


def country_zones_sort_step_2(wb, url_link):
    authorization_to_admin_page(wb, url_link)

    countries_list_with_zone = []

    countries_row = browser.find_elements_by_css_selector("form table tbody tr.row")
    count_country = len(countries_row)
    count_test = 0

    for i in countries_row:
        country = i.find_element_by_css_selector("td:not([style]) a")
        countries_link = country.get_attribute("href")
        countries_list_with_zone.append(countries_link)
    for i in countries_list_with_zone:
        zones_list = []
        browser.get(i)
        zones_row = browser.find_elements_by_xpath(".//*[@class='dataTable']/tbody/tr/td/"
                                                   "select[contains(@name, 'zones[')]/"
                                                   "option[@selected='selected' and not(@data-phone-code)]")
        for j in zones_row[1:len(zones_row)-1]:
            zones_list.append(j.text)
        sorted_zones_list = sorted(zones_list)
        if sorted_zones_list == zones_list:
            count_test += 1

    assert count_test == count_country, 'Zones are not sorted'


try:
    country_zones_sort_step_1(browser, url_step_1)
    country_zones_sort_step_2(browser, url_step_2)
finally:
    browser.quit()

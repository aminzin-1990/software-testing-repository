from selenium import webdriver
import time

link = "https://ya.ru"

browser = webdriver.Chrome()
browser.get(link)
time.sleep(5)
browser.quit()

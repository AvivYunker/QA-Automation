from lib2to3.pgen2 import driver
import time
from selenium import webdriver
browser = webdriver.Chrome()

browser.get('http://orteil.dashnet.org/cookieclicker/')
time.sleep(3)

got_it_button = browser.find_element_by_link_text('Got it!')
got_it_button.click()

big_cookie_button = browser.find_element_by_id('bigCookie')
for cnt in range(0, 300, 1):
    big_cookie_button.click()
time.sleep(20)

browser.quit()

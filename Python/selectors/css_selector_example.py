import time
from selenium import webdriver
from selenium.webdriver.common.alert import Alert
browser = webdriver.Chrome()

browser.get('https://techstepacademy.com/training-ground')
time.sleep(3)

# elements
text_input_field_1 = browser.find_element_by_css_selector('#ipt1')
text_input_field_2 = browser.find_element_by_css_selector('#ipt2')
button_1 = browser.find_element_by_css_selector('#b1')
button_2 = browser.find_element_by_css_selector('#b2')
button_3 = browser.find_element_by_css_selector('#b3')
button_4 = browser.find_element_by_css_selector('#b4')
# actions
text_input_field_1.send_keys("sample text...")

button_1.click()
alert = Alert(browser)
alert.accept()

button_2.click()
alert = Alert(browser)
alert.accept()

text_input_field_2.send_keys("sample text...")

button_3.click()
alert = Alert(browser)
alert.accept()

button_4.click()
alert = Alert(browser)
alert.accept()

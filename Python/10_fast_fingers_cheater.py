import time
from selenium import webdriver
from selenium.webdriver.common.alert import Alert
browser = webdriver.Chrome()

browser.get('https://10fastfingers.com')
time.sleep(3)
allow_all_cookies_button = browser.find_element_by_id('CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll')
allow_all_cookies_button.click()

start_typing_test_button = browser.find_element_by_id('typing-test')
start_typing_test_button.click()
long_list = browser.find_element_by_id('row1')
all_words = list(long_list.find_elements_by_tag_name('span'))

input_word_field = browser.find_element_by_id('inputfield')

for cnt in range(0, len(all_words), 1):
    word = all_words[cnt].text
    input_word_field.send_keys(word + ' ')
input_word_field.clear()

#print("all_words is: " + str(all_words))
time.sleep(1000)
browser.quit()
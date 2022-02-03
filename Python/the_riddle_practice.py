import time
from selenium import webdriver
browser = webdriver.Chrome()

browser.get('https://techstepacademy.com/trial-of-the-stones')

riddle_of_stone_text_field = browser.find_element_by_id('r1Input')
answer_button_1 = browser.find_element_by_id('r1Btn')
riddle_of_stone_text_field.send_keys('rock')
answer_button_1.click()
answer_1_text = browser.find_element_by_xpath('//*[@id="passwordBanner"]/h4').text

riddle_of_secrets_text_field = browser.find_element_by_id('r2Input')
answer_button_2 = browser.find_element_by_id('r2Butn')
riddle_of_secrets_text_field.send_keys(answer_1_text)
answer_button_2.click()
answer_2_text = browser.find_element_by_xpath('//*[@id="successBanner1"]/h4')

merchant_1_name = browser.find_element_by_xpath('//*[@id="block-05ea3afedc551e378bdc"]/div/div[3]/span/b').text
merchant_1_wealth = browser.find_element_by_xpath('//*[@id="block-05ea3afedc551e378bdc"]/div/div[3]/p').text
merchant_2_name = browser.find_element_by_xpath('//*[@id="block-05ea3afedc551e378bdc"]/div/div[4]/span/b').text
merchant_2_wealth = browser.find_element_by_xpath('//*[@id="block-05ea3afedc551e378bdc"]/div/div[4]/p').text
richest_merchant_answer = browser.find_element_by_id('r3Input')
answer_button_3 = browser.find_element_by_id('r3Butn')

richest_merchant = ""
if (int(merchant_1_wealth) > int(merchant_2_wealth)):
    richest_merchant = str(merchant_1_name)
elif (int(merchant_1_wealth) < int(merchant_2_wealth)):
    richest_merchant = str(merchant_2_name)
else:
    richest_merchant = "neither"

richest_merchant_answer.send_keys(richest_merchant)
answer_button_3.click()

check_answers_button = browser.find_element_by_id('checkButn')
check_answers_button.click()
final_results = browser.find_element_by_xpath('//*[@id="successBanner2"]/h4').text

if (final_results == 'Success!'):
    print("\nV\n")
else:
    print('\nX\n')

# print("the final text was: " + str(final_results))
import time
from selenium import webdriver
browser = webdriver.Chrome()

browser.get('https://www.saucedemo.com/')

# PAGE 1 (elements)
user_name_text_field = browser.find_element_by_id('user-name')
password_text_field = browser.find_element_by_id('password')
login_button = browser.find_element_by_id('login-button')

# PAGE 1 (actions)
user_name_text_field.send_keys('standard_user')
password_text_field.send_keys('secret_sauce')
login_button.click()

# PAGE 2 (elements)
sauce_labs_backpack_add_to_cart_button = browser.find_element_by_id('add-to-cart-sauce-labs-backpack')
sauce_labs_bike_light_add_to_cart_button = browser.find_element_by_id('add-to-cart-sauce-labs-bike-light')
sauce_labs_bolt_t_shirt_add_to_cart_button = browser.find_element_by_id('add-to-cart-sauce-labs-bolt-t-shirt')
sauce_labs_fleece_jacket_add_to_cart_button = browser.find_element_by_id('add-to-cart-sauce-labs-fleece-jacket')
sauce_labs_onesie_add_to_cart_button = browser.find_element_by_id('add-to-cart-sauce-labs-onesie')
sauce_labs_red_t_shirt_add_to_cart_button = browser.find_element_by_id('add-to-cart-test.allthethings()-t-shirt-(red)')
shopping_cart_button = browser.find_element_by_class_name('shopping_cart_link')

# PAGE 2 (actions)
sauce_labs_backpack_add_to_cart_button.click()
sauce_labs_bike_light_add_to_cart_button.click()
sauce_labs_bolt_t_shirt_add_to_cart_button.click()
sauce_labs_fleece_jacket_add_to_cart_button.click()
sauce_labs_onesie_add_to_cart_button.click()
sauce_labs_red_t_shirt_add_to_cart_button.click()
shopping_cart_button.click()

# PAGE 3 (elements)
checkout_button = browser.find_element_by_id('checkout')

# PAGE 3 (actions)
checkout_button.click()

# PAGE 4 (elements)
first_name_text_field = browser.find_element_by_id('first-name')
last_name_text_field = browser.find_element_by_id('last-name')
postal_code_text_field = browser.find_element_by_id('postal-code')
continue_button = browser.find_element_by_id('continue')

# PAGE 4 (actions)
first_name_text_field.send_keys('first')
last_name_text_field.send_keys('last')
postal_code_text_field.send_keys('12345')
continue_button.click()

# PAGE 5 (elements)
finish_button = browser.find_element_by_id('finish')

# PAGE 5 (actions)
finish_button.click()

# PAGE 6 (elements)
success_message = browser.find_element_by_css_selector('#checkout_complete_container > h2').text

# PAGE 6 (actions)
if (success_message == 'THANK YOU FOR YOUR ORDER'):
    print("\n\nV\n\n")
else:
    print("\n\nV\n\n")

# print('the message was: ' + str(success_message))
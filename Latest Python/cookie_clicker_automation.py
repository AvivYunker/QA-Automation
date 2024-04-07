# importing all necessary tools & libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pyautogui
import random

def attempt_purchase():
    purchase_type = random.randint(0,9)
    if (purchase_type < 8):
        for cnt in range(len(actual_purchaseables)-1, -1, -1):
            if (actual_purchaseables[cnt].get_attribute('class') == "product locked disabled toggledOff") or (actual_purchaseables[cnt].get_attribute('class') == "product locked disabled"):
                continue
            else:
                actual_purchaseables[cnt].click()
    else:
        for cnt in range(len(purchaseable_upgrades)-1, -1, -1):
            purchaseable_upgrades[cnt].click()

# configure webdriver and initial setup
driver = webdriver.Chrome()
driver.get('https://orteil.dashnet.org/cookieclicker/')
time.sleep(0.5)
driver.maximize_window()
time.sleep(0.5)

# accept cookies
got_it = driver.find_element(By.XPATH, "//a[text()='Got it!']")
time.sleep(0.25)
got_it.click()

# selecting English
english_option = driver.find_element(By.XPATH, "//div[text()='English']")
time.sleep(0.5)
english_option.click()
time.sleep(1)

# main functionality
time.sleep(5)
cookie = driver.find_element(By.XPATH, "//button[@id='bigCookie']")
actual_purchaseables = driver.find_elements(By.XPATH, "//span[@class='price']/../..")
purchasable_names = driver.find_elements(By.XPATH, "//span[@class='price']/..//div[@class='title productName']")
purchasable_prices = driver.find_elements(By.XPATH, "//span[@class='price']")
purchaseable_upgrades = driver.find_elements(By.XPATH, "//div[@id='upgrades']//div")
for cnt in range(0, 100000, 1):
    cookie.click()
    if (cnt % 100 == 0):
        attempt_purchase()

backery_name = driver.find_element(By.XPATH, "//div[@id='storeTitle']")

time.sleep(0.1)
assert backery_name.text == "Store", f"🔴 Automated test failed. 🔴"
print(f"\n🟢 Quiz has been automatically completed successfully 🟢\n")
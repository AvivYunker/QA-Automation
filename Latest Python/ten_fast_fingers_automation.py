# importing all necessary tools & libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pyautogui

# configure webdriver and initial setup
driver = webdriver.Chrome()
driver.get('https://10fastfingers.com/')
time.sleep(0.25)
driver.maximize_window()
time.sleep(3)

try:
    allow_all = driver.find_element(By.XPATH, "//button[text()='Allow all']")
    time.sleep(0.25)
    allow_all.click()
except:
    pass

# login to app with registered user
login_button = driver.find_element(By.XPATH, "//a[@id='login-register']")
time.sleep(0.25)
login_button.click()
time.sleep(2)

try:
    close_video_add_button = driver.find_element(By.XPATH, "//div[@id='closeIconHit']")
    time.sleep(0.25)
    close_video_add_button.click()
except:
    pass



USERNAME = "forqaautomation@gmail.com"
PASSWORD = "GreyFox002"
username_field = driver.find_element(By.XPATH, "//label[text()='Email']/..//input")
password_field = driver.find_element(By.XPATH, "//label[text()='Password']/..//input")
login_button = driver.find_element(By.XPATH, "//button[text()='Login']")
time.sleep(0.25)
username_field.send_keys(USERNAME)
password_field.send_keys(PASSWORD)
login_button.click()

word_list = []
word_input = driver.find_element(By.XPATH, "//input[@type='text']")
raw_words = driver.find_elements(By.XPATH, "//div[@id='row1']//span")
for word in raw_words:
    word_input.send_keys(word.get_attribute("innerText"))
    word_input.send_keys(" ")
    time.sleep(0.05)
word_input.clear()

time.sleep(30)
pyautogui.press("ESC")

time.sleep(5)
result_header = driver.find_element(By.XPATH, "//h3[text()='Result ']")

time.sleep(0.1)
assert result_header.get_attribute("innerText") == "Result Screenshot", f"🔴 Automated test failed. 🔴'-{result_header.get_attribute("innerText")}-"
print(f"\n🟢 Quiz has been automatically completed successfully 🟢\n")
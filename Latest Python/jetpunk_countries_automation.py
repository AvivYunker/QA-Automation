# importing all necessary tools & libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pyautogui

# configuring necessary data for program flow
Europe = ['Albania','Andorra','Austria','Belarus','Belgium','Bosnia','Bulgaria','Croatia','Czech Republic','Denmark','Estonia','Finland','France','Germany','Greece','Hungary','Iceland','Ireland','Italy','Kosovo','Latvia','Liechtenstein','Lithuania','Luxembourg','Malta','Moldova','Monaco','Montenegro','Netherlands','Macedonia','Norway','Poland','Portugal','Romania','Russia','San Marino','Serbia','Slovakia','Slovenia','Spain','Sweden','Switzerland','UK','Ukraine','Vatican']
Asia = ['Afghanistan','Armenia','Azerbaijan','Bahrain','Bangladesh','Bhutan','Brunei','Cambodia','China','Cyprus','East Timor','Georgia','India','Indonesia','Iran','Iraq','Israel','Japan','Jordan','Kazakhstan','Kuwait','Kyrgyzstan','Laos','Lebanon','Malaysia','Maldives','Mongolia','Myanmar','Nepal','North Korea','Oman','Pakistan','Philippines','Qatar','Saudi Arabia','Singapore','South Korea','Sri Lanka','Syria','Taiwan','Tajikistan','Thailand','Turkey','Turkmenistan','UAE','Uzbekistan','Vietnam','Yemen']
Africa = ['Algeria','Angola','Benin','Botswana','Burkina Faso','Burundi','Cameroon','Cape Verde','CAR','Chad','Comoros','Congo','Djibouti','Egypt','Equatorial Guinea','Eritrea','Eswatini','Ethiopia','Gabon','Gambia','Ghana','Guinea','Guinea Bissau','Ivory Coast','Kenya','Lesotho','Liberia','Libya','Madagascar','Malawi','Mali','Mauritania','Mauritius','Morocco','Mozambique','Namibia','Niger','Nigeria','Rwanda','Sao Tome','Senegal','Seychelles','Sierra Leone','Somalia','South Africa','South Sudan','Sudan','Tanzania','Togo','Tunisia','Uganda','Zambia','Zimbabwe']
North_America = ['Antigua','Bahamas','Barbados','Belize','Canada','Costa Rica','Cuba','Dominica','Dominican Republic','El Salvador','Grenada','Guatemala','Haiti','Honduras','Jamaica','Mexico','Nicaragua','Panama','Saint Kitts','Saint Lucia','Saint Vincent','Trinidad','United States']
South_America = ['Argentina','Bolivia','Brazil','Chile','Colombia','Ecuador','Guyana','Paraguay','Peru','Suriname','Uruguay','Venezuela']
Oceania = ['Australia','Micronesia','Fiji','Kiribati','Marshall Islands','Nauru','New Zealand','Palau','Papua New Guinea','Samoa','Solomon Islands','Tonga','Tuvalu','Vanuatu']

continents = [Europe, Asia, Africa, North_America, South_America, Oceania]

# configure webdriver and initial setup
driver = webdriver.Chrome()
driver.get('https://www.jetpunk.com/')
time.sleep(0.5)
driver.maximize_window()
time.sleep(0.5)

# locating and clicking the login button
login_button = driver.find_element(By.XPATH, "//div[@title='Login']//button[text()='Login']")
login_button.click()

# locating username, password fields and login button, and logging into valid user
username_field = driver.find_element(By.XPATH, "//div[text()='Login to Your Account']/../..//label[text()='Screen name or Email:']/..//input")
password_field = driver.find_element(By.XPATH, "//div[text()='Login to Your Account']/../..//label[text()='Password:']/..//input")
login_button = driver.find_element(By.XPATH, "//div[text()='Login to Your Account']/../..//button[text()='Login']")
time.sleep(0.5)
USERNAME = "forqaautomation@gmail.com"
PASSWORD = "GreyFox001"
username_field.send_keys(USERNAME)
password_field.send_keys(PASSWORD)
time.sleep(0.25)
login_button.click()
time.sleep(0.5)
okay_button = driver.find_element(By.XPATH, "//button[text()='Okay']")
time.sleep(0.25)
okay_button.click()


# navigate to the countries quiz and locate necessary elements
driver.get('https://www.jetpunk.com/user-quizzes/63858/countries-of-the-world-one-minute-sprint')
time.sleep(3)
driver.execute_script("window.scrollTo(0,400)")
start_quiz_button = driver.find_element(By.XPATH, "//button[@id='start-button']")
time.sleep(0.25)
start_quiz_button.click()
time.sleep(0.25)
answer_textbox = driver.find_element(By.XPATH, "//input[@id='txt-answer-box']")

time.sleep(0.25)
for continent in continents:
    for country in continent:
        #print(country)
        answer_textbox.send_keys(country)
        answer_textbox.send_keys(" ")
        time.sleep(0.03)

time.sleep(3)
pyautogui.press("ESC")

time.sleep(0.1)
user_score = driver.find_element(By.XPATH, "//span[@class='user-score']")

time.sleep(0.1)
assert user_score.text == "196", f"🔴 Automated test failed. 🔴"
print(f"\n🟢 Quiz has been automatically completed successfully 🟢\n")
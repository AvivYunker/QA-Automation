import time
from selenium import webdriver
from selenium.webdriver.common.alert import Alert
browser = webdriver.Chrome()


Europe = ['Albania','Andorra','Austria','Belarus','Belgium','Bosnia','Bulgaria','Croatia','Czech Republic','Denmark','Estonia','Finland','France','Germany','Greece','Hungary','Iceland','Ireland','Italy','Kosovo','Latvia','Liechtenstein','Lithuania','Luxembourg','Malta','Moldova','Monaco','Montenegro','Netherlands','Macedonia','Norway','Poland','Portugal','Romania','Russia','San Marino','Serbia','Slovakia','Slovenia','Spain','Sweden','Switzerland','UK','Ukraine','Vatican']
Asia = ['Afghanistan','Armenia','Azerbaijan','Bahrain','Bangladesh','Bhutan','Brunei','Cambodia','China','Cyprus','East Timor','Georgia','India','Indonesia','Iran','Iraq','Israel','Japan','Jordan','Kazakhstan','Kuwait','Kyrgyzstan','Laos','Lebanon','Malaysia','Maldives','Mongolia','Myanmar','Nepal','North Korea','Oman','Pakistan','Philippines','Qatar','Saudi Arabia','Singapore','South Korea','Sri Lanka','Syria','Taiwan','Tajikistan','Thailand','Turkey','Turkmenistan','UAE','Uzbekistan','Vietnam','Yemen']
Africa = ['Algeria','Angola','Benin','Botswana','Burkina Faso','Burundi','Cameroon','Cape Verde','CAR','Chad','Comoros','Congo','Djibouti','Egypt','Equatorial Guinea','Eritrea','Eswatini','Ethiopia','Gabon','Gambia','Ghana','Guinea','Guinea Bissau','Ivory Coast','Kenya','Lesotho','Liberia','Libya','Madagascar','Malawi','Mali','Mauritania','Mauritius','Morocco','Mozambique','Namibia','Niger','Nigeria','Rwanda','Sao Tome','Senegal','Seychelles','Sierra Leone','Somalia','South Africa','South Sudan','Sudan','Tanzania','Togo','Tunisia','Uganda','Zambia','Zimbabwe']
North_America = ['Antigua','Bahamas','Barbados','Belize','Canada','Costa Rica','Cuba','Dominica','Dominican Republic','El Salvador','Grenada','Guatemala','Haiti','Honduras','Jamaica','Mexico','Nicaragua','Panama','Saint Kitts','Saint Lucia','Saint Vincent','Trinidad','United States']
South_America = ['Argentina','Bolivia','Brazil','Chile','Colombia','Ecuador','Guyana','Paraguay','Peru','Suriname','Uruguay','Venezuela']
Oceania = ['Australia','Micronesia','Fiji','Kiribati','Marshall Islands','Nauru','New Zealand','Palau','Papua New Guinea','Samoa','Solomon Islands','Tonga','Tuvalu','Vanuatu']


continents = [Europe, Asia, Africa, North_America, South_America, Oceania]

browser.get('https://www.jetpunk.com/user-quizzes/63858/countries-of-the-world-one-minute-sprint')
time.sleep(0.5)
browser.maximize_window()
time.sleep(0.5)

login_button = browser.find_element_by_xpath('//*[@id="inner-page"]/div[1]/div/div[2]/div[2]/div[3]/button')
login_button.click()

username_field = browser.find_element_by_xpath('//*[@id="login-modal"]/div/div[2]/div[1]/input')
password_field = browser.find_element_by_xpath('//*[@id="login-modal"]/div/div[2]/div[2]/input')
login_button = browser.find_element_by_xpath('//*[@id="login-modal"]/div/div[2]/div[3]/button')

username_field.send_keys("") # DON'T FORGET TO INSERT USERNAME
password_field.send_keys("") # DON'T FORGET TO INSERT PASSWORD
login_button.click()

browser.get('https://www.jetpunk.com/user-quizzes/63858/countries-of-the-world-one-minute-sprint')
time.sleep(0.5)

browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
time.sleep(0.5)

start_quiz_button = browser.find_element_by_id('start-button')
start_quiz_button.click()

answer_text_box = browser.find_element_by_id('txt-answer-box')

for countries in continents:
    for country in countries:
        answer_text_box.send_keys(country)
        if (len(answer_text_box.text) >= 20):
            print(answer_text_box.text)


time.sleep(50)
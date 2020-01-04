import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from dotenv import load_dotenv
load_dotenv()

import os

WEBDRIVER_PATH = os.getenv('WEBDRIVER_PATH')
LOGIN = os.getenv('INSTAGRAM_EMAIL')
PASSWORD = os.getenv('INSTAGRAM_PASSWORD')

driver = webdriver.Chrome(executable_path=WEBDRIVER_PATH)
driver.implicitly_wait(10)
driver.get("https://www.instagram.com/accounts/login/?hl=pt-br&source=auth_switcher")

elem = driver.find_element_by_name("username")
elem.send_keys(LOGIN)

elem = driver.find_element_by_name("password")
elem.send_keys(PASSWORD)
elem.send_keys(Keys.RETURN)

time.sleep(5)
elem = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/section/div[3]/div[1]/div/div[2]/div[1]/a')
username = elem.text

driver.get("https://www.instagram.com/{0}".format(username))
time.sleep(3)

elem = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/ul/li[2]/a')
elem.click()
time.sleep(2)

elem = driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/ul')
friends = elem.find_elements_by_tag_name('ul')
print(len(friends))
print(friends)

driver.close()
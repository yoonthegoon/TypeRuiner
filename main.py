import time
from selenium import webdriver
from selenium.webdriver.common.by import By


# Race your friends
# text_path = '/html/body/div[1]/div/div[1]/div/div[1]/div[2]/table/tbody/tr[2]/td[2]/div/div[1]/table/tbody/tr[3]/td/div/div/table/tbody/tr[2]/td[3]/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr[1]/td/div/div'
# Pubs
text_path = '/html/body/div[1]/div/div[1]/div/div[1]/div[2]/table/tbody/tr[2]/td[2]/div/div[1]/div/table/tbody/tr[2]/td[3]/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr[1]/td/div/div'

driver = webdriver.Firefox()
driver.implicitly_wait(1)
driver.get('https://play.typeracer.com')

input('start')
# Race your friends
# enter_typing_race = driver.find_element(By.CLASS_NAME, 'raceAgainLink')
# Pubs
enter_typing_race = driver.find_element(By.XPATH, '//a[@title="Keyboard shortcut: Ctrl+Alt+I"]')
enter_typing_race.click()

text = driver.find_element(By.XPATH, text_path)
txt_input = driver.find_element(By.CLASS_NAME, 'txtInput')

kps = 12 / (int(input('wpm: ')) / .7)
for char in text.text:
    time.sleep(kps)
    txt_input.send_keys(char)

input('stop')
driver.close()

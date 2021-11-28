from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Firefox()
driver.get('https://monkeytype.com/')

input('start')
type_input = driver.find_element(By.XPATH, '//input[@id="wordsInput"]')
while True:
    word = driver.find_element(By.XPATH, '//div[@class="word active"]')
    type_input.send_keys(word.text, ' ')

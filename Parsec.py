from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pickle



driver = webdriver.Edge()

driver.get('https://yandex.ru/images/search?text=cat')
#Cat = driver.find_element(By.CLASS_NAME, 'Cat')



input()

driver.quit()
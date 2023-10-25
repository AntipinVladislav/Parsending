from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pickle

edge_driver_path = 'C:\Bydon (piton)\MicrosoftWebDriver.exe'
service_1 = Service(edge_driver_path)

service_1.start()

driver = webdriver.Edge(edge_driver_path)

driver.get('https://yandex.ru/images/search?text=cat')
Cat = driver.find_element(By.CLASS_NAME, 'Cat')

with open("saved_image.pickle", "wb") as f:
    # Dump the image data into the file using pickle
    pickle.dump(Cat, f)

driver.quit()


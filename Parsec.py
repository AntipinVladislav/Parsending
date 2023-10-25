from selenium import webdriver




driver = webdriver.Edge()

driver.get('https://yandex.ru/images/search?text=cat')
#Cat = driver.find_element(By.CLASS_NAME, 'Cat')



input()

driver.quit()
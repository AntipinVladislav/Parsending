from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
from pathlib import Path
import time
from selenium.webdriver.common.action_chains import ActionChains




# name_id = 0
# driver = webdriver.Edge()
# actions = ActionChains(driver)

# Path("dataset/Cats").mkdir(parents=True, exist_ok=True)
# driver.get('https://unsplash.com/s/photos/cat?license=free')
# time.sleep(2)


# for i in range(51):
#     if i == 1:
#         load_more_button = driver.find_element(By.XPATH, '//button[text()="Load more"]')
#         actions.click(load_more_button).perform()

#     actions.scroll_by_amount(0, 10000).perform()
#     actions.scroll_by_amount(0, -500).perform()
#     time.sleep(1)

# download_link_elements = driver.find_elements(By.XPATH, '/descendant::a[@data-test="non-sponsored-photo-download-button"]')
# download_links = list(map(lambda x: x.get_attribute('href'), download_link_elements))
# for link in download_links:
#     r = requests.get(link, stream=True)
#     if r.status_code == 200:
#         with open(f'dataset/Cats/{str(name_id).zfill(4)}.jpg', 'wb') as f:
#             for chunk in r.iter_content(1024):
#                 f.write(chunk)
#     name_id+=1
    

# driver.get('https://unsplash.com/s/photos/dog?license=free')
# Path("dataset/Dogs").mkdir(parents=True, exist_ok=True)
# time.sleep(2)
# name_id = 0

# for i in range(51):
#     if i == 1:
#         load_more_button = driver.find_element(By.XPATH, '//button[text()="Load more"]')
#         actions.click(load_more_button).perform()

#     actions.scroll_by_amount(0, 10000).perform()
#     actions.scroll_by_amount(0, -500).perform()
#     time.sleep(1)

# download_link_elements = driver.find_elements(By.XPATH, '/descendant::a[@data-test="non-sponsored-photo-download-button"]')
# download_links = list(map(lambda x: x.get_attribute('href'), download_link_elements))
# for link in download_links:
#     r = requests.get(link, stream=True)
#     if r.status_code == 200:
#         with open(f'dataset/Dogs/{str(name_id).zfill(4)}.jpg', 'wb') as f:
#             for chunk in r.iter_content(1024):
#                 f.write(chunk)
#     name_id+=1

# print('END OF LIFE')
# input()

# driver.quit()


name_id = 0
driver = webdriver.Edge()
actions = ActionChains(driver)

Path("dataset1/Cats").mkdir(parents=True, exist_ok=True)
driver.get('https://yandex.ru/images/search?from=tabbar&text=cats')
time.sleep(2)


for i in range(51):
    
    actions.scroll_by_amount(0, 10000).perform()
    actions.scroll_by_amount(0, -500).perform()
    time.sleep(1)

photo_link_elements = driver.find_elements(By.XPATH, '/descendant::a[@class="Link SimpleImage-Cover"]')
photo_links = list(map(lambda x: x.get_attribute('href'), photo_link_elements))




for photo in photo_links:
    driver.get(photo)
    time.sleep(0.5)
    download_link_elements = driver.find_elements(By.XPATH, '/html/body/div[14]/div[2]/div/div/div/div[3]/div/div[1]/div[3]/div/div/div[1]/div[4]/div[1]/a')
    download_links = list(map(lambda x: x.get_attribute('href'), download_link_elements))
    for link in download_links:
        r = requests.get(link, stream=True)
        if r.status_code == 200:
            with open(f'dataset1/Cats/{str(name_id).zfill(4)}.jpg', 'wb') as f:
                for chunk in r.iter_content(1024):
                    f.write(chunk)
        name_id+=1



Path("dataset1/Dogs").mkdir(parents=True, exist_ok=True)
driver.get('https://yandex.ru/images/search?from=tabbar&text=dogs')
time.sleep(2)
name_id = 0

photo_link_elements = driver.find_elements(By.XPATH, '/descendant::a[@class="Link SimpleImage-Cover"]')
photo_links = list(map(lambda x: x.get_attribute('href'), photo_link_elements)) 

for photo in photo_links:
    driver.get(photo)
    time.sleep(0.5)
    download_link_elements = driver.find_elements(By.XPATH, '/html/body/div[14]/div[2]/div/div/div/div[3]/div/div[1]/div[3]/div/div/div[1]/div[4]/div[1]/a')
    download_links = list(map(lambda x: x.get_attribute('href'), download_link_elements))
    for link in download_links:
        r = requests.get(link, stream=True)
        if r.status_code == 200:
            with open(f'dataset1/Dogs/{str(name_id).zfill(4)}.jpg', 'wb') as f:
                for chunk in r.iter_content(1024):
                    f.write(chunk)
        name_id+=1

print('END OF LIFE')
input()

driver.quit()
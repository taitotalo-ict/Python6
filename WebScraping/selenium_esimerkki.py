from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get('https://google.com')

button = driver.find_element(By.ID, 'L2AGLb')
button.click()

search_box = driver.find_element(By.NAME, 'q')
search_box.send_keys('python')
search_box.submit()
time.sleep(60)
# drive.page_source # Sivun lähdekoodi

driver.close()
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get('https://www.google.com/?hl=pt_BR')

campo = driver.find_element(By.NAME, 'q')

driver.quit()

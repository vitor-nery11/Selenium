from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()

driver.get('https://www.google.com/?hl=pt_BR')

campo = driver.find_element(By.NAME, 'q')

campo.send_keys('Curso selenium Python')
time.sleep(5)

driver.quit()


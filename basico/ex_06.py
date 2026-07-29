from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

driver.get('https://www.google.com/?hl=pt_BR')

campo = driver.find_element(By.NAME, 'q')

campo.send_keys('FastAPI')
time.sleep(3)

botao = driver.find_element(By.NAME, 'btnK')
print(botao.is_displayed())
print(botao.is_enabled())
botao.click()

time.sleep(3)

driver.quit()

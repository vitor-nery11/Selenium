from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

driver.get('https://www.google.com/?hl=pt_BR')

campo = driver.find_element(By.NAME,'q')

campo.send_keys('FastAPI')
time.sleep(2)
campo.send_keys(Keys.ENTER)
time.sleep(3)


driver.quit()


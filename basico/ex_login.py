from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()

driver.get('https://www.saucedemo.com/')

campo = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, 'user-name'))
)

campo.send_keys('standard_user')

campo = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, 'password'))
)

campo.send_keys('secret_sauce')

botao = WebDriverWait(driver,10).until(
    EC.element_to_be_clickable((By.ID, 'password'))
)

botao.send_keys(Keys.ENTER)

input('aperte enter para finalizar:')

driver.quit()





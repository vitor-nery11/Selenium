from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()

driver.get('https://www.saucedemo.com/')

campo_usuario = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, 'user-name'))
)

campo_usuario.send_keys('standard_user')

campo_senha = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, 'password'))
)

campo_senha.send_keys('secret_sauce')

botao_login = WebDriverWait(driver,10).until(
    EC.element_to_be_clickable((By.ID, 'login-button'))
)

botao_login.click()

titulo = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.CLASS_NAME, 'title'))
)

texto_titulo = titulo.text

print(titulo.text)

assert texto_titulo == 'Products'

print('Titulo continua o mesmo')


input('aperte enter para finalizar:')

driver.quit()

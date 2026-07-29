from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def esperar_elemento(driver, estrategia, valor):
    elemento = WebDriverWait(driver,10).until(
        EC.presence_of_element_located((estrategia, valor))
    )

    return elemento

def preencher_campo(driver, estrategia, valor, texto):
    elemento = esperar_elemento(driver, estrategia, valor)
    elemento.send_keys(texto)

# AÇÃO 

driver = webdriver.Chrome()

driver.get('https://www.saucedemo.com/')

preencher_campo(driver,By.ID, 'user-name','standard_user')

input('aperte enter para finalizar:')

driver.quit()

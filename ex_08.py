from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get('https://www.google.com')

# Espera o campo de pesquisa estar visivel
campo = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, 'q'))
)

# Digita na barra de pesquisa
campo.send_keys('Biblia')

# Aperta o botão enter
campo.send_keys(Keys.ENTER)

input('Aperte a tecla enter para finalizar:')

driver.quit()



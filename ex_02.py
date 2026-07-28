from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get('https://www.linkedin.com/in/vitor-nery-dev/')
time.sleep(3)

driver.switch_to.new_window('tab')

driver.get('https://www.youtube.com/')
time.sleep(3)

driver.quit()
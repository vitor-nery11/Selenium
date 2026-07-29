from pages.login_page import LoginPage
from selenium import webdriver

driver = webdriver.Chrome()

login = LoginPage(driver)

login.fazer_login('vtnery', '123456')

input('aperte enter:')

driver.quit()

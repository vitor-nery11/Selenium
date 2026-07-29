from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.usuario = (By.ID, "user-name")
        self.senha = (By.ID, "password")
        self.botao_login = (By.ID, "login-button")

    def fazer_login(self, usuario, senha):
        print(usuario)
        print(senha)
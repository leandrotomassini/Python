import random
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options

class Platzi:

    def __init__(self):
        self.escuelas = []

    def agregarEscuelas(self):
        driver = webdriver.Chrome()
        driver.get('https://platzi.com')
        driver.close()

    def verEscuelas(self):
        for escuela in self.escuelas:
            print(escuela)


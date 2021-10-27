from Escuela import Escuela
from Navegador import Navegador
from selenium.webdriver.common.by import By

class Platzi:

    escuelas = []
    navegador = ""

    def __init__(self):
        self.navegador = Navegador()

    def verEscuelas(self):
        self.obtenerEscuelas()
        for escuela in self.escuelas:
            print(escuela)

    def obtenerEscuelas(self):
        driver = self.navegador.abrirNavegador("https://platzi.com")
        self.escuelas = driver.driver.find_elements(By.XPATH, '//p[@class="SchoolsList-school-description"]/strong')
        print(self.escuelas)
        driver.close()
import random
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options

class Navegador:
    opts = ""
    driver = ""

    def __init__(self):
        self.opts = Options()
        self.opts.add_argument("USER_AGENT=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.80 Chrome/71.0.3578.80 Safari/537.36")
        self.driver = webdriver.Chrome('./chromedriver.exe', chrome_options=self.opts)

    def abrirNavegador(self, url):
        self.driver.get(url)
        return self.driver
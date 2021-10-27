import random
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import os

listadoEscuelas = []

opts = Options()
opts.add_argument(
    "USER_AGENT=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.80 Chrome/71.0.3578.80 Safari/537.36"
)

driver = webdriver.Chrome('./chromedriver.exe', chrome_options=opts)

driver.get("https://platzi.com")

escuelas = driver.find_elements(By.XPATH, '//a[@class="SchoolsList-school"]')

i = 0

for escuela in escuelas:
    i += 1
    nombre = escuela.find_element(By.XPATH, './/strong').text
    url = escuela.get_attribute('href')
    print(i, nombre, ' - ', url)
    nombreCarpeta = "E://" + str(i) + ' - ' + nombre.title()
    directorio = (nombreCarpeta)
    try:
        os.mkdir(directorio)
    except OSError:
        print("La creación del directorio %s falló" % directorio)
    else:
        print("Se ha creado el directorio: %s " % directorio)

    listadoEscuelas.append(url)
    f = open('E://Escuelas-URL.txt', 'a')
    f.write( url + '\n')
    f.close()


driver.get('file:///F:/descarga.htm')


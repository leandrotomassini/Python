import random
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.olx.com.ec/autos_c378")

for i in range(3):
    try:
        boton = driver.find_element(By.XPATH, '//button[@data-aut-id="btnLoadMore"]')
        boton.click()
        sleep(random.uniform(8.0, 10.0))
    except:
        break

autos = driver.find_elements(By.XPATH, '//li[@data-aut-id="itemBox"]')
autos = driver.find_elements(By.XPATH, '//li[@data-aut-id="itemBox"]')

for auto in autos:
    precio = auto.find_element(By.XPATH, './/span[@data-aut-id="itemPrice"]').text
    descripcion = auto.find_element(By.XPATH, './/span[@data-aut-id="itemTitle"]').text
    print(descripcion)
    print(precio)
    print()


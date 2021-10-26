from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.olx.com.ec/")

for i in range(3):
    try:
       boton = WebDriverWait(driver, 10).until(EC.presence_of_element_located(By.XPATH, '//button[@data-aut-id="btnLoadMore"]'))
       boton.click()
       WebDriverWait(driver, 10).until(
           EC.presence_of_element_located(By.XPATH, '//li[@data-aut-id="itemBox"]//span[@data-aut-id="itemPrice"]')
       )
    except:
        break


anuncios = driver.find_elements(By.XPATH, '//li[@data-aut-id="itemBox"]')

for anuncio in anuncios:
    precio = anuncio.find_element(By.XPATH, './/span[@data-aut-id="itemPrice"]').text
    descripcion = anuncio.find_element(By.XPATH, './/span[@data-aut-id="itemTitle"]').text
    print(descripcion)
    print(precio)
    print()


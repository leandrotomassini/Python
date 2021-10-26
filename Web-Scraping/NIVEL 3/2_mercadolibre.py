from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options


opts = Options()
opts.add_argument(
    "USER_AGENT=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.80 Chrome/71.0.3578.80 Safari/537.36"
)
driver = webdriver.Chrome('./chromedriver.exe', chrome_options=opts)

driver.get('https://listado.mercadolibre.com.ec/repuestos-autos-camionetas-bujias')


while True:
    links_productos = driver.find_elements(By.XPATH, '//a[contains(@class,"ui-search-item__group__element ui-search-link")]')
    links_de_la_pagina = []
    for tag_a in links_productos:
        links_de_la_pagina.append(tag_a.get_attribute("href"))

    for link in links_de_la_pagina:
        try:
            driver.get(link)
            titulo = driver.find_element(By.XPATH, "//h1[contains(@class, 'ui-pdp-title')]").text
            precio = driver.find_element(By.XPATH, "//span[contains(@class, 'price-tag-fraction')]").text
            print(titulo)
            print(precio)
            driver.back()
        except Exception as e:
            print("Error: ", e)
            driver.back()

    try:
        boton_siguiente = driver.find_element(By.XPATH, "//span[contains(@class, 'andes-pagination__arrow-title')]")
        boton_siguiente.click()
    except:
        break
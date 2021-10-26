import random
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options

scrollingScript = "document.getElementsByClassName('')[0].scroll(0, 20000)"

opts = Options()
opts.add_argument(
    "USER_AGENT=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.80 Chrome/71.0.3578.80 Safari/537.36"
)

driver = webdriver.Chrome('./chromedriver.exe', chrome_options=opts)
driver.get("https://www.google.com/maps/place/Restaurante+Taiga+Madrid/@40.4379173,-3.6902495,15z/data=!4m11!1m2!2m1!1srestaurante!3m7!1s0xd42292e6da3ee07:0x5221c57b765bde46!8m2!3d40.4371217!4d-3.6796362!9m1!1b1!15sCgtyZXN0YXVyYW50ZVoNIgtyZXN0YXVyYW50ZZIBCnJlc3RhdXJhbnQ")

sleep(random.uniform(4.0, 5.0))

SCROLLS = 0
while(SCROLLS != 3):
    driver.execute_script()
    sleep(random.uniform(5, 6))
    SCROLLS += 1

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys

driver=webdriver.Chrome()
driver.get('https://yandex.ru')
wait =  WebDriverWait(driver, 60).until(EC.presence_of_element_located(( By.CLASS_NAME, 'home-logo__default'))) #Дождемся появления картинки
driver.quit()
sys.exit()

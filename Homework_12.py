from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys
import string
import random
import time
import os

def code_generator(size, chars=string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

driver = webdriver.Chrome()
try:
    driver.get('http://litecart.stqa.ru/admin/')
    driver.find_element_by_name('username').send_keys('admin')
    driver.find_element_by_name('password').send_keys('0b7dba1c77df25bf0')
    driver.find_element_by_name('login').click()
    driver.find_element_by_link_text('Catalog').click()
    driver.find_element_by_css_selector('a[href $="edit_product"]').click()
    time.sleep(2)
    driver.find_element_by_css_selector('input[value = "1"]').click()
    driver.find_element_by_name('name[en]').send_keys(code_generator(10, string.ascii_lowercase))
    driver.find_element_by_name('code').send_keys(code_generator(6))
    driver.find_element_by_name('quantity').clear()
    driver.find_element_by_name('quantity').send_keys(code_generator(3))
    items = driver.find_elements_by_css_selector("input[name='product_groups[]']")
    for item in  items:
             item.click()
    driver.find_element_by_css_selector('td > input[value = "1-3"]').click
    driver.find_element_by_name('new_images[]').send_keys(os.getcwd()+"/avatar512.jpg")
    driver.find_element_by_link_text('Information').click()
    driver.find_element_by_css_selector('select[name = "manufacturer_id"]').click()
    driver.find_element_by_css_selector('select[name = "manufacturer_id"] option[value = "1"]').click()
    driver.find_element_by_name('keywords').send_keys(code_generator(5, string.ascii_lowercase))
    driver.find_element_by_name('short_description[en]').send_keys(code_generator(13, string.ascii_lowercase))
    driver.find_element_by_css_selector('div.trumbowyg-editor').send_keys(code_generator(130, string.ascii_lowercase))
    driver.find_element_by_name('short_description[en]').send_keys(code_generator(7, string.ascii_lowercase))
    driver.find_element_by_name('meta_description[en]').send_keys(code_generator(7, string.ascii_lowercase))
    driver.find_element_by_name('head_title[en]').send_keys(code_generator(7, string.ascii_lowercase))
    driver.find_element_by_css_selector('a[href $="prices"]').click()
    time.sleep(2)
    driver.find_element_by_name('purchase_price').clear()
    driver.find_element_by_name('purchase_price').send_keys(code_generator(3))
    driver.find_element_by_css_selector('select[name = "purchase_price_currency_code"]').click()
    driver.find_element_by_css_selector('select[name = "purchase_price_currency_code"] option[value = "USD"]').click()
    driver.find_element_by_name('prices[USD]').send_keys(code_generator(3))
    driver.find_element_by_name('prices[EUR]').send_keys(code_generator(3))
    driver.find_element_by_name('save').click()
    driver.quit()
    print('Тест пройден!')
    sys.exit()
except Exception as e:
    print('Тест не пройден!', e)
    sys.exit()
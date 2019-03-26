from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get('http://litecart.stqa.ru/en/')
array = ['Yellow Duck'] #Желтой уточки нет в продаже, мы ее покупать не будем)))
for i in range(1,4):
    driver.find_element_by_css_selector('li.product a[title $="Duck"]').click()
    while driver.find_element_by_css_selector('h1').text in array: #Если такую уточку покупали, то выберем другую.
       driver.back()                                               #И будем выбирать, пока не попадется новая
       driver.find_element_by_css_selector('li.product a[title $="Duck"]').click()
    array.append(driver.find_element_by_css_selector('h1').text)
    driver.find_element_by_name('add_cart_product').click()
    WebDriverWait(driver, 5).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, 'span.quantity'), str(i)))
    driver.back()
driver.find_element_by_css_selector('a[href $="checkout"]').click()
for i in range(8,5, -1):                                          #Очищаем корзину
    driver.find_element_by_name('remove_cart_item').click()       # жмем на кнопку ...
                                                                  #... ищем последнию строку таблицы...
                                                                  # ждем, пока она не уйдет из DOM
    item = driver.find_element_by_css_selector('table.dataTable > tbody > tr:nth-child('+str(i)+')')
    WebDriverWait(driver, 5).until(EC.staleness_of(item))






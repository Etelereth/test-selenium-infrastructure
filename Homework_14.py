from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys

driver = webdriver.Chrome()
driver.get('http://litecart.stqa.ru/admin/') #Заходим в админку...
try: #... и пытаемся залогиниться
    login = driver.find_element_by_name('username')
    login.send_keys('admin')
    pwd = driver.find_element_by_name('password')
    pwd.send_keys('0b7dba1c77df25bf0')
    enter = driver.find_element_by_name('login')
    enter.click()
except Exception as e:
    print('Что-то пошло не так', e)
    driver.quit()
try:
    driver.find_element_by_css_selector('a[href $="doc=countries"]').click()
    driver.find_element_by_css_selector('a[href $="code=BB"]').click()
    items = driver.find_elements_by_css_selector('i.fa-external-link')   #Находим ссылки ведущие в нове окно
    for item in items:
        current_window = driver.window_handles                           #Сохраним текущее
        item.click()
        WebDriverWait(driver, 10).until(EC.new_window_is_opened(current_window))
        new_window = driver.window_handles                               #Немного волшебства с массивами, чтобы выбрать новое окно
        new_window.remove(driver.current_window_handle)
        driver.switch_to.window(new_window[0])                           #Переклоючимся в новое
        WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located((By.TAG_NAME, 'body'))) #Немного подождем
        driver.close()                                                    #Закроем
        driver.switch_to.window(current_window[0])                        #Вернемся
    print('Тест пройден')
except Exception as e:
    print('Тест не пройден, ошибка:',e)

driver.quit()
sys.exit()

from selenium import webdriver
import sys

driver = webdriver.Chrome()
driver.get('http://litecart.stqa.ru/admin/')
try:
    login = driver.find_element_by_name('username')
    login.send_keys('admin')
    pwd = driver.find_element_by_name('password')
    pwd.send_keys('0b7dba1c77df25bf0')
    enter = driver.find_element_by_name('login')
    enter.click()
except Exception as e:
    print('Что-то пошло не так', e)
    driver.quit()


driver.get("http://litecart.stqa.ru/admin/?app=catalog&doc=catalog&category_id=1&query=Duck")
items = driver.find_elements_by_partial_link_text('Duck')
links = []
for item in items:
    links.append(item.get_attribute('href'))
for link in links:
    selector = 'a[href ="'+link+'"]'
    driver.find_element_by_css_selector(selector).click()
    if len(driver.get_log('browser')) > 0:
       for log in driver.get_log('browser'):
           print('Лог::', log)
    else:
        print('Логов нет')
    driver.back()
driver.quit()
sys.exit()
from selenium import webdriver
import sys

driver=webdriver.Chrome()
driver.get('http://10.77.252.9/litecart/public_html/admin')
try:
    login = driver.find_element_by_name('username')
    login.send_keys('admin')
    pwd = driver.find_element_by_name('password')
    pwd.send_keys('admin')
    enter = driver.find_element_by_name('login')
    enter.click()
    assert 'My Store' in driver.title
    driver.quit()
    print('Page loaded')
except Exception as e:
    print('Что-то пошло не так', e)
    driver.quit()
sys.exit()
from selenium import webdriver
import sys
import time


driver=webdriver.Chrome()
driver.get('http://10.77.252.9/litecart/public_html/admin')
#залогинимся
try:
    login = driver.find_element_by_name('username')
    login.send_keys('admin')
    pwd = driver.find_element_by_name('password')
    pwd.send_keys('admin')
    enter = driver.find_element_by_name('login')
    enter.click()
    assert 'My Store' in driver.title
except Exception as e:
    print('Что-то пошло не так', e)
    driver.quit()
try:
    items = driver.find_elements_by_css_selector('li#app-')
except Exception as e:
    print('Наверное, нет элементов', e)
    driver.quit()
lenght = len(items)
for i in range(0,lenght):
    try:
        items = driver.find_elements_by_css_selector('li#app-')
        items[i].click()
        title = driver.find_element_by_css_selector('h1')
        if title.text=='':
            print('Страница без заголовка')
        else:
            print(title.text)
        subitems = driver.find_elements_by_css_selector('li[id ^=doc-]')
        if len(subitems) >0:
            for j in range(0, len(subitems)):
                subitems = driver.find_elements_by_css_selector('li[id ^=doc-]')
                subitems[j].click()
                title = driver.find_element_by_css_selector('h1')
                if title.text == '':
                    print('Страница без заголовка')
                else:
                    print(title.text)
    except Exception as e:
        print('На элемент не удалось кликнуть', e )
        driver.quit()
driver.quit()
sys.exit()

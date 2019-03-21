from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sys

driver=webdriver.Chrome()
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

driver.get('http://litecart.stqa.ru/admin/?app=countries&doc=countries')
items = driver.find_elements_by_css_selector('tr.row')
list_country = []                                                   # возьмем пустой массив

for item in items:
    list_zones = []
    sub_items = item.find_elements_by_css_selector('td')                     #найдем все поля строки
    list_country.append(sub_items[4].text)
    # Наполним его странами
    if sub_items[5].text != '0':                                             # Если в стране есть зоны
        item.find_element_by_css_selector('a').send_keys(Keys.CONTROL + Keys.ENTER)            #Откроем новую вклдаку
        driver.switch_to.window(driver.window_handles[1])                    #А в ней уже все проверим
        other_items = driver.find_elements_by_css_selector('table#table-zones tr:not(.header) td:nth-child(3)')

        for other_item in other_items:
            if other_item.text != '':
                list_zones.append(other_item.text)

        driver.close()
        driver.switch_to.window(driver.window_handles[0])
                                                                             #Закроем  вкладку, проверим порядок
        if sorted(list_zones) == list_zones:
            print('Зоны', sub_items[4].text, 'идут по алфавиту')
        else:
            print('Зоны', sub_items[4].text, 'идут не по алфавиту')
                                                                             # И продолжим смотреть по стнранам
'''
Мне жутко не хотелось разбираться где хранить элементы, т.к. при переходе на другую страницу и возвращении обратно 
получается. страница обновится. Я подумал, что можно перейти на другую вкладку, там все
просмотреть и вернуться на предыдущую, на которой элементы остануться неизменными.
'''

if sorted(list_country) == list_country:
    print('Все страны идут по алфавиту')
else:
    print ('Страны идут не по алфавиту')
# Выводим результат
#--------------------------------------------------------------------------

#Аналогично для второй части задания

driver.get('http://litecart.stqa.ru/admin/?app=geo_zones&doc=geo_zones')
items = driver.find_elements_by_css_selector('tr.row a:not([title=Edit])')
for item in items:
    list_zones = []
    item.send_keys(Keys.CONTROL + Keys.ENTER)
    driver.switch_to.window(driver.window_handles[1])
    sub_items = driver.find_elements_by_css_selector('select[name *=zone_code] option[selected]')

    for sub_item in sub_items:
        list_zones.append(sub_item.text)

    driver.close()
    driver.switch_to.window(driver.window_handles[0])

    if sorted(list_zones) == list_zones:
        print('Зоны', item.text, 'идут по алфавиту')
    else:
        print('Зоны', item.text, 'идут не по алфавиту\n',list_zones,'\n',sorted(list_zones))
driver.close()
sys.exit()


from selenium import webdriver
import sys
import re

class duck:
    name = ''
    reg_price = ''
    reg_price_color = []
    reg_price_font =''
    reg_price_line = ''
    camp_price = ''
    camp_price_color= []
    camp_price_font = ''
    camp_price_bold = ''

def str2rgb(s):
    rgba = re.sub('[a-z()]','',s).split(",")
    if len(rgba) not in (3, 4):
        return (0, 0, 0)
    return tuple(map(int, rgba))

def duck_info(item):
    duck1=duck()
    try:
       duck1.name =  item.find_element_by_class_name('name').text
    except:
        duck1.name = item.find_element_by_css_selector('h1.title').text
    duck1.reg_price = item.find_element_by_class_name('regular-price').text
    duck1.reg_price_color=str2rgb(item.find_element_by_class_name('regular-price').value_of_css_property('color'))
    duck1.reg_price_font = item.find_element_by_class_name('regular-price').value_of_css_property('font-size')
    duck1.reg_price_line = item.find_element_by_class_name('regular-price').value_of_css_property('text-decoration')
    duck1.camp_price = item.find_element_by_class_name('campaign-price').text
    duck1.camp_price_color = str2rgb(item.find_element_by_class_name('campaign-price').value_of_css_property('color'))
    duck1.camp_price_font = item.find_element_by_class_name('campaign-price').value_of_css_property('font-size')
    duck1.camp_price_bold =  item.find_element_by_class_name('campaign-price').value_of_css_property('font-weight')
    return duck1

def gray_color(duck):
    if duck.reg_price_color[0] == duck.reg_price_color[1] == duck.reg_price_color[2]:
        return True
    else:
        return False

def red_color(duck):
    if  duck.camp_price_color[1] == 0 and duck.camp_price_color[2] == 0:
        return True
    else:
        return False

def main_check(driver):
    driver.get('http://litecart.stqa.ru/en/') #Заходим на главную
    item = driver.find_element_by_css_selector('a[title="Yellow Duck"]')   # Тк. не все товары имеют акционную цену, выбираем тот, у кого она точно есть

    duck1 = duck()
    duck1 = duck_info(item)
    item.click()
    item = driver.find_element_by_css_selector('div#box-product')
    duck2 = duck()
    duck2 = duck_info(item)
    driver.quit()

    if duck1.name == duck2.name:
        print('Тест А пройден, имена совпадают')
    else:
        print('Тест А  не пройден, имена не совпадают')

    if duck1.reg_price == duck2.reg_price:
        print('Тест Б.1 пройден, обычная цена совпадает')
    else:
        print('Тест Б.1  не пройден, обычная цена не совпадает')

    if duck1.camp_price == duck2.camp_price:
        print('Тест Б.2 пройден, акционная цена совпадает')
    else:
        print('Тест Б.2  не пройден, акционная цена совпадает')

    if gray_color(duck1):
        print('Тест В.1 пройден, обычная цена серая')
    else:
        print('Тест В.1  не пройден, обычная цена не серая')

    if gray_color(duck2):
        print('Тест В.2 пройден, обычная цена серая')
    else:
        print('Тест В.2  не пройден, обычная цена не серая')

    if duck1.reg_price_line.split(' ')[0]=='line-through':
        print('Тест В.3 пройден, обычная цена зачеркнута')
    else:
        print('Тест В.3  не пройден, обычная цена не зачеркнута')

    if duck2.reg_price_line.split(' ')[0]=='line-through':
        print('Тест В.4 пройден, обычная цена зачеркнута')
    else:
        print('Тест В.4  не пройден, обычная цена не зачеркнута')

    if red_color(duck1):
        print('Тест Г.1 пройден, акционная цена красная')
    else:
        print('Тест Г.1  не пройден, акционная цена не красная')

    if red_color(duck2):
        print('Тест Г.2 пройден, акционная цена красная')
    else:
        print('Тест Г.2  не пройден, акционная цена не красная')
    
    if int(re.sub('\D','',duck1.camp_price_bold)) >= 700:
        print('Тест Г.3 пройден, акционная цена жирная')
    else:
        print('Тест Г.3  не пройден, акционная цена не жирная')

    if int(re.sub('\D','',duck2.camp_price_bold)) >= 700:
        print('Тест Г.4 пройден, акционная цена жирная')
    else:
        print('Тест Г.4  не пройден, акционная цена не жирная')

    if float(re.sub('[a-z]','',duck1.reg_price_font)) < float(re.sub('[a-z]','',duck1.camp_price_font)):
       print('Тест Д.1 пройден, акционная цена больше')
    else:
       print('Тест Д.1 не пройден, акционная цена не больше')

    if float(re.sub('[a-z]', '', duck2.reg_price_font)) < float(re.sub('[a-z]', '', duck2.camp_price_font)):
        print('Тест Д.2 пройден, акционная цена больше')
    else:
        print('Тест Д.2 не пройден, акционная цена не больше')

print('\n\n================Google Chrome==================')
main_check(webdriver.Chrome())
print('\n================Mozilla Firefox================')
main_check(webdriver.Firefox())
print('\n================Internet Explorer==============')
main_check(webdriver.Ie())
sys.exit()


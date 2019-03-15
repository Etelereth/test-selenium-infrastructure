from selenium import webdriver
import sys
#Однако, есть предположение, что я не понял задание
driver=webdriver.Chrome()
driver.get('http://litecart.stqa.ru/en/') #Заходим на главную
items = driver.find_elements_by_css_selector('li[class ^=product]') #Ищем уточек
i = with_sticker = with_2stickers = without_sticker = 0
for item in items:                                                   #Перебираем их
   i+=1
   try:
    sticker = item.find_elements_by_css_selector('div[class ^=sticker]')  #Ищем в каждой точке стикер
    if len(sticker) == 1:
        print('Уточка',item.text, 'со стикером',sticker[0].text)          #Если находим
        with_sticker +=1
    elif len(sticker) >1:
        print('Уточка', item.text,'имеет 2 и больше стикеров')            #если находим, но много
        with_2stickers +=1
    elif len(sticker) == 0:
        print('Уточка', item.text,' не имеет стикера')                    #Если ничего не находим
        without_sticker+=1
   except Exception as e:
       print('Что-то пошло не так', e.args)
#Выводим итог
print('\n\n\nВсего проверено уточек',i,', из них:\nсо стикером',with_sticker,'\nбез стикера:',without_sticker,'\n2 и более стикеров:',with_2stickers)
driver.quit()
sys.exit


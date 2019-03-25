from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys
import string
import random

# Заполним рандомом
domains = [ "hotmail.com", "gmail.com", "aol.com", "mail.com" , "mail.kz", "yahoo.com"]
letters = string.ascii_lowercase[:12]


def code_generator(size, chars=string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def get_one_random_domain(domains = [ "hotmail.com", "gmail.com", "aol.com", "mail.com" , "mail.kz", "yahoo.com"]):
    return random.choice(domains)

def get_one_random_name(letters = string.ascii_lowercase[:12] ):
    return ''.join(random.choice(letters) for i in range(7))

def generate_random_email():
    return get_one_random_name(letters) + '@' + get_one_random_domain(domains)

driver = webdriver.Chrome()
driver.get('http://litecart.stqa.ru/en/create_account')
try:

    driver.find_element_by_name('firstname').send_keys(get_one_random_name())
    driver.find_element_by_name('lastname').send_keys(get_one_random_name())
    driver.find_element_by_name('address1').send_keys(get_one_random_name())
    driver.find_element_by_name('postcode').send_keys(code_generator(5))
    driver.find_element_by_name('city').send_keys(get_one_random_name())
    driver.find_element_by_css_selector('span.selection').click()
    driver.find_element_by_css_selector('input.select2-search__field').send_keys('united states', Keys.ENTER)
    driver.find_element_by_css_selector('select[name = "zone_code"]').click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located(( By.CSS_SELECTOR, 'select[name = "zone_code"] option[value = "MA"]'))) # нужна небольшая задержка
    driver.find_element_by_css_selector('select[name = "zone_code"] option[value = "MA"]').click()
    driver.find_element_by_name('phone').send_keys(code_generator(11))
    email = generate_random_email()
    driver.find_element_by_name('email').send_keys(email)
    password = get_one_random_name()
    driver.find_element_by_name('password').send_keys(password)
    driver.find_element_by_name('confirmed_password').send_keys(password)
    #print(email, password)
    driver.find_element_by_name('create_account').click()
    driver.find_element_by_link_text('Logout').click()
    driver.find_element_by_name('email').send_keys(email)
    driver.find_element_by_name('password').send_keys(password)
    driver.find_element_by_name('login').click()
    driver.find_element_by_link_text('Logout').click()
    driver.quit()
    print('Тест выполнен')
except Exception as e:
    print('Тест не выполнен:')
sys.exit()
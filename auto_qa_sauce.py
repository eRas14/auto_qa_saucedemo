# Напишите скрипт для работы с интернет-магазином. Шаги
# 1. Открыть сайт магазина https://www.saucedemo.com/
# 2. Авторизоваться под пользователем standard_user
# 3. Добавить в корзину товары:
#     1. Sauce Labs Backpack
#     2. Saue Labs Bolt T-Shirt
#     3. Sauce Labs Onesie

# 4. Перейти в корзину
# 5. Нажать Checkout
# 6. Заполнить форму данными:
#     1. Имя
#     2. Фамиля
#     3. Почтовый индекс
# 7. Нажать continue
# 7. Прочитать со стрницы итоговую стоимость ( Total )
# 8. Закрыть браузер
# 9. Вывести в консоль итоговую стоимость

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Firefox()
waiter = WebDriverWait(browser, 60)

browser.get('https://www.saucedemo.com/')

#ввод логина и пароля
browser.find_element(By.CSS_SELECTOR, '#user-name').send_keys("standard_user")
browser.find_element(By.CSS_SELECTOR, '#password').send_keys("secret_sauce")

#клик на кнопку
browser.find_element(By.CSS_SELECTOR, '#login-button').click()

#список кнопок к добавлени товара
items = ["#add-to-cart-sauce-labs-backpack", "#add-to-cart-sauce-labs-bolt-t-shirt", "#add-to-cart-sauce-labs-onesie"]

#циклом добавляем товары в корзину
for item in items:
    browser.find_element(By.CSS_SELECTOR, item).click()

#переход в корзину
browser.find_element(By.CSS_SELECTOR, '.shopping_cart_link').click()

#нажатие чекаут
browser.find_element(By.CSS_SELECTOR, '#checkout').click()

#Заполнение форм

#Определение словаря с селекторами и значениями
user_info = {
    '#first-name': 'Albert',
    '#last-name': 'Urazov',
    '#postal-code': '460048'
}

# Итерация по ключам словаря
for selector, value in user_info.items():
    browser.find_element(By.CSS_SELECTOR, selector).send_keys(value)

#нажатие контин
browser.find_element(By.CSS_SELECTOR, '#continue').click()

#Отображение итоговой стоимости
total_cost = browser.find_element(By.CSS_SELECTOR, '.summary_total_label').text

print(f'Итоговая стоимость - {total_cost}')

#нажатие finish
browser.find_element(By.CSS_SELECTOR, '#finish').click()



browser.quit()
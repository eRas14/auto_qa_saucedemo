# Данный автотест имитирует поведение пользователя на сайте интернет-магазина Saucedemo, выполнено в стиле спагетти кода.
## Тест включает в себя авторизацию:    
### -Добавление товаров в корзину
### -Заполнение формы для оформления заказа 
### -Извлечение итоговой стоимости

```

from selenium import webdriver
from selenium.webdriver.common.by import By


browser = webdriver.Firefox()
browser.implicitly_wait(4)

browser.get('https://www.saucedemo.com/')

#ввод логина и пароля
browser.find_element(By.CSS_SELECTOR, '#user-name').send_keys("standard_user")
browser.find_element(By.CSS_SELECTOR, '#password').send_keys("secret_sauce")

#клик на кнопку
browser.find_element(By.CSS_SELECTOR, '#login-button').click()

items_to_add = ["Sauce Labs Backpack", "Sauce Labs Bolt T-Shirt", "Sauce Labs Onesie"]

items = browser.find_elements(By.CSS_SELECTOR, '.inventory_item')

for item in items:
    if item.find_element(By.CSS_SELECTOR, ".inventory_item_name").text in items_to_add:
        item.find_element(By.CSS_SELECTOR, "button").click()


# #список кнопок к добавлени товара
# items = ["#add-to-cart-sauce-labs-backpack", "#add-to-cart-sauce-labs-bolt-t-shirt", "#add-to-cart-sauce-labs-onesie"]

# #циклом добавляем товары в корзину
# for item in items:
#     browser.find_element(By.CSS_SELECTOR, item).click()

# #переход в корзину
# browser.find_element(By.CSS_SELECTOR, '.shopping_cart_link').click()

browser.get("https://www.saucedemo.com/cart.html")

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

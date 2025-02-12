from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Запуск браузера
driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/inputs")

# Найти поле ввода
input_field = driver.find_element(By.TAG_NAME, "input")

# Тест 1: Ввод числа
input_field.send_keys("12345")
time.sleep(1)
print(f"Тест 1 (число): {input_field.get_attribute('value')}")  # Должно быть "12345"

# Очистка поля
input_field.clear()

# Тест 2: Ввод дробного числа
input_field.send_keys("12.34")
time.sleep(1)
print(f"Тест 2 (дробное число): {input_field.get_attribute('value')}")  # Должно быть "12.34"

input_field.clear()

# Тест 3: Ввод букв (проверка валидации)
input_field.send_keys("abc")
time.sleep(1)
print(f"Тест 3 (буквы): {input_field.get_attribute('value')}")  # Должно быть пусто, если валидация работает

input_field.clear()

# Тест 4: Ввод спецсимволов
input_field.send_keys("@#$%^&*")
time.sleep(1)
print(f"Тест 4 (спецсимволы): {input_field.get_attribute('value')}")  # Должно быть пусто

input_field.clear()

# Тест 5: Граничные значения (очень большое число)
input_field.send_keys("999999999999999999999")
time.sleep(1)
print(f"Тест 5 (очень большое число): {input_field.get_attribute('value')}")  # Должно быть ограничено

input_field.clear()

# Завершение теста
driver.quit()

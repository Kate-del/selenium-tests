from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Запуск браузера
driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/inputs")

def test_input(value, description):
    input_field = driver.find_element(By.TAG_NAME, "input")
    input_field.clear()
    input_field.send_keys(value)
    time.sleep(1)  # Ожидание для визуального контроля
    print(f"Тест {description}: {input_field.get_attribute('value')}")

# 1️⃣ Ввод обычного числа
test_input("12345", "(число)")
# 2️⃣ Ввод дробного числа
test_input("12.34", "(дробное число)")
# 3️⃣ Ввод букв (не должно приниматься)
test_input("abc", "(буквы)")
# 4️⃣ Ввод спецсимволов (не должно приниматься)
test_input("@#$%^", "(спецсимволы)")
# 5️⃣ Ввод очень большого числа
test_input("999999999999999999999", "(очень большое число)")
# 6️⃣ Ввод отрицательного числа
test_input("-123", "(отрицательное число)")
# 7️⃣ Ввод пустой строки
test_input("", "(пустое поле)")
# 8️⃣ Ввод числа с пробелами (перед и после)
test_input("   123   ", "(число с пробелами)")
# 9️⃣ Тест на удаление символов
input_field = driver.find_element(By.TAG_NAME, "input")
input_field.clear()
input_field.send_keys("12345")
time.sleep(1)
input_field.send_keys(Keys.BACKSPACE * 5)
time.sleep(1)
print(f"Тест (удаление символов): {input_field.get_attribute('value')}")
# 🔟 Ввод максимально длинного числа
test_input("123456789012345678901234567890", "(максимальная длина числа)")

# Закрываем браузер
driver.quit()

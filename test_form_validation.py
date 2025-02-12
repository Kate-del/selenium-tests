from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Запуск браузера
driver = webdriver.Chrome()

# Открываем страницу логина
driver.get("https://the-internet.herokuapp.com/login")

# Пауза, чтобы страница полностью загрузилась
time.sleep(2)

# Тест 1: Попытка входа с пустыми полями
login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
login_button.click()

# Ждём появления сообщения об ошибке
time.sleep(2)
error_message = driver.find_element(By.ID, "flash").text
print(f"Ошибка при пустых полях: {error_message}")

# Тест 2: Ввод некорректных данных
username_field = driver.find_element(By.ID, "username")
password_field = driver.find_element(By.ID, "password")

username_field.send_keys("wrong_user")
password_field.send_keys("wrong_password")

# Повторно находим кнопку, так как старая ссылка могла устареть
login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
login_button.click()

# Ждём появления сообщения
time.sleep(2)
error_message = driver.find_element(By.ID, "flash").text
print(f"Ошибка при неправильных данных: {error_message}")

# Тест 3: Корректный вход
username_field = driver.find_element(By.ID, "username")
password_field = driver.find_element(By.ID, "password")

# Очищаем поля перед вводом
username_field.clear()
password_field.clear()

username_field.send_keys("tomsmith")
password_field.send_keys("SuperSecretPassword!")

# Повторно находим кнопку перед кликом
login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
login_button.click()

# Ждём появления сообщения
time.sleep(2)
success_message = driver.find_element(By.ID, "flash").text
print(f"Сообщение при успешном входе: {success_message}")

# Закрываем браузер
driver.quit()

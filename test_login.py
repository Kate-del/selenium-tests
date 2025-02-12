from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Запускаем браузер
driver = webdriver.Chrome()

try:
    # Открываем страницу логина
    driver.get("https://the-internet.herokuapp.com/login")

    # Находим поля ввода и вводим данные
    username = driver.find_element(By.ID, "username")
    password = driver.find_element(By.ID, "password")
    
    username.send_keys("tomsmith")  # Правильный логин
    password.send_keys("SuperSecretPassword!")  # Правильный пароль
    password.send_keys(Keys.RETURN)

    time.sleep(3)  # Даем странице загрузиться

    # Проверяем успешный вход
    success_message = driver.find_element(By.CLASS_NAME, "flash").text
    assert "You logged into a secure area!" in success_message

    print("✅ Тест успешного логина пройден!")

finally:
    driver.quit()  # Закрываем браузер

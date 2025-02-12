from selenium import webdriver
from selenium.webdriver.common.by import By

# Инициализация браузера
driver = webdriver.Chrome()

try:
    driver.get("https://the-internet.herokuapp.com/")  

    # Проверяем кнопки
    buttons = driver.find_elements(By.TAG_NAME, "button")
    for button in buttons:
        assert button.is_enabled(), f"Кнопка {button.text} неактивна!"

    # Проверяем ссылки
    links = driver.find_elements(By.TAG_NAME, "a")
    for link in links:
        href = link.get_attribute("href")
        assert href is not None, f"Ссылка без href: {link.text}"
        print(f"Ссылка '{link.text}' ведет на {href}")

    print("✅ Тест кнопок и ссылок пройден успешно!")

finally:
    driver.quit()

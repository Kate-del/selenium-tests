from selenium import webdriver

# Указываем путь к chromedriver (замени на свой путь!)
driver = webdriver.Chrome()

# Открываем сайт Google
driver.get("https://www.google.com")

# Закрываем браузер
driver.quit()

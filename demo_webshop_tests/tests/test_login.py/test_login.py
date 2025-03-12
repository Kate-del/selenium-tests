import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Фикстура для инициализации браузера
@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

# Тест успешного логина
def test_successful_login(browser):
    browser.get("https://demowebshop.tricentis.com/login")

    # Вводим email
    browser.find_element(By.ID, "Email").send_keys("czukanova17@bk.ru")

    # Вводим пароль
    browser.find_element(By.ID, "Password").send_keys("test123" + Keys.RETURN)

    # Ожидание редиректа на главную страницу
    WebDriverWait(browser, 10).until(EC.url_to_be("https://demowebshop.tricentis.com/"))

    # Ожидание появления кнопки "Log out"
    log_out = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.LINK_TEXT, "Log out")))
    
    assert log_out.is_displayed()

# Тест неверного логина
def test_invalid_login(browser):
    browser.get("https://demowebshop.tricentis.com/login")

    browser.find_element(By.ID, "Email").send_keys("wrong@example.com")
    browser.find_element(By.ID, "Password").send_keys("wrongpassword" + Keys.RETURN)

    # Проверяем наличие сообщения об ошибке
    error_message = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".validation-summary-errors"))
    ).text
    assert "Login was unsuccessful" in error_message

# Тест логаута
def test_logout(browser):
    browser.get("https://demowebshop.tricentis.com/login")

    # Логинимся
    browser.find_element(By.ID, "Email").send_keys("czukanova17@bk.ru")
    browser.find_element(By.ID, "Password").send_keys("test123" + Keys.RETURN)

    # Ожидание появления кнопки "Log out"
    log_out = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.LINK_TEXT, "Log out")))
    log_out.click()

    # Ожидание появления кнопки "Log in"
    WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.LINK_TEXT, "Log in")))

    assert browser.find_element(By.LINK_TEXT, "Log in").is_displayed()

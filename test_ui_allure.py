import pytest
from selenium import webdriver
import allure

@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@allure.feature("Форма входа")
def test_login_valid_data(driver):
    with allure.step("Открываем страницу логина"):
        driver.get("https://the-internet.herokuapp.com/login")

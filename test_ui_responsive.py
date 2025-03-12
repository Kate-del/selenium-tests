from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import pytest

# Разрешения экранов для проверки
SCREEN_SIZES = [(1920, 1080), (1366, 768), (1024, 768), (375, 667)]

@pytest.mark.parametrize("width,height", SCREEN_SIZES)
def test_responsive_design(width, height):
    options = Options()
    options.add_argument("--headless")  # Запуск без UI
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    
    try:
        driver.set_window_size(width, height)
        driver.get("https://example.com")  # Заменить на нужный сайт
        
        # Проверка заголовка страницы
        assert "Example" in driver.title, "Страница загрузилась некорректно"
        
        # Сделать скриншот (можно использовать для сравнения)
        driver.save_screenshot(f"screenshot_{width}x{height}.png")
    
    finally:
        driver.quit()

if __name__ == "__main__":
    pytest.main(["-v", "--tb=short"])

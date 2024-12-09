import pytest
from selenium import webdriver

from config.app import test_app_config
from tests.utils.api_client import APIClient


@pytest.fixture(scope="function")
def browser():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--remote-debugging-port=9222")
    options.add_argument("--disable-extensions")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--disable-software-rasterizer")

    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()


@pytest.fixture(scope="session")
def api_client():
    # Базовый URL из .env
    base_url = test_app_config.sites_config.api_url
    return APIClient(base_url)

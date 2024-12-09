import allure
import pytest
from tests.ui.pages.main_page import MainPage


@pytest.mark.ui
@allure.suite("AQA Tests")
@allure.feature("UI Tests")
@allure.story("Main Page UI")
class TestMainPage:

    @allure.title("Проверка открытия главной страницы")
    @allure.description("Тест проверяет открытие главной страницы сайта.")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.open_main_page
    def test_open_main_page(self, browser):
        """Тест проверяет открытие главной страницы сайта."""
        main_page = MainPage(browser)
        with allure.step("Открываем главную страницу"):
            main_page.open_main_page()
        with allure.step("Проверяем заголовок страницы"):
            assert "STORE" in browser.title, "Заголовок страницы некорректен"

    @allure.title("Проверка списка продуктов")
    @allure.description("Тест проверяет отображение списка продуктов на главной странице.")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.product_list
    def test_product_list(self, browser):
        """Тест проверяет отображение списка продуктов на главной странице."""
        main_page = MainPage(browser)
        with allure.step("Открываем главную страницу"):
            main_page.open_main_page()
        with allure.step("Получаем список продуктов"):
            products = main_page.get_product_titles()
        with allure.step("Проверяем, что список продуктов не пуст"):
            assert len(products) > 0, "Список продуктов пуст"

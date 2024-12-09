import pytest
import allure


@pytest.mark.api
@allure.suite("AQA Tests")
@allure.feature("API Tests")
@allure.story("Test Posts API")
class TestPosts:

    @allure.title("Получение всех постов")
    @allure.description("Тест проверяет, что можно успешно получить список всех постов.")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.get_posts
    def test_get_all_posts(self, api_client):
        with allure.step("Отправка GET запроса на /posts"):
            response = api_client.get("/posts")
        with allure.step("Проверка статуса ответа"):
            assert response.status_code == 200, "Некорректный статус-код для GET /posts"
        with allure.step("Проверка, что список постов не пустой"):
            assert len(response.json()) > 0, "Список постов пуст"
        with allure.step("Проверка структуры поста"):
            assert "userId" in response.json()[0], "Поле 'userId' отсутствует в данных поста"

    @allure.title("Создание нового поста")
    @allure.description("Тест проверяет возможность создания нового поста через POST запрос.")
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.create_post
    def test_create_post(self, api_client):
        payload = {
            "title": "foo",
            "body": "bar",
            "userId": 1
        }
        with allure.step("Отправка POST запроса с данными поста"):
            response = api_client.post("/posts", data=payload)
        with allure.step("Проверка статуса ответа"):
            assert response.status_code == 201, "Некорректный статус-код для POST /posts"
        with allure.step("Проверка, что созданный пост соответствует отправленным данным"):
            assert response.json()["title"] == payload[
                "title"], "Заголовок созданного поста не совпадает с отправленным"

    @allure.title("Удаление поста")
    @allure.description("Тест проверяет успешное удаление поста через DELETE запрос.")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.delete_post
    def test_delete_post(self, api_client):
        with allure.step("Отправка DELETE запроса на /posts/1"):
            response = api_client.delete("/posts/1")
        with allure.step("Проверка статуса ответа"):
            assert response.status_code == 200, "Некорректный статус-код для DELETE /posts/1"

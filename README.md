# AQA-automation-tests
Demonstration project on automated testing

## Описание проекта
Этот проект предназначен для автоматизации тестирования с использованием следующих инструментов и технологий:
- **Python**: для написания тестов.
- **Pytest**: для управления тестовыми запусками.
- **Selenium**: для UI-тестов.
- **Allure**: для генерации отчетов.
- **JMeter**: для нагрузочного тестирования.
- **Docker**: для изоляции окружения.
- **Docker Compose**: для управления несколькими сервисами.

---

## Тестируемые системы
1. **UI-тесты**:
    - Сайт: [Demoblaze](https://www.demoblaze.com)
    - Цель: тестирование пользовательского интерфейса.

2. **API-тесты**:
    - Сервис: [JSONPlaceholder](https://jsonplaceholder.typicode.com)
    - Цель: тестирование функционала REST API.

3. **Нагрузочное тестирование**:
    - Сервис: [JSONPlaceholder](https://jsonplaceholder.typicode.com)
    - Цель: оценка производительности под нагрузкой.

---

## Требования
Перед запуском проекта убедитесь, что на вашем компьютере установлены:
- [Python 3.9+](https://www.python.org/)
- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)
- [Git](https://git-scm.com/)

---

## Установка

1. Клонируйте репозиторий:
   ```bash
   git clone git@github.com:MorozovMikeDeveloper/AQA-automation-tests.git
   cd AQA-automation-tests

2. Создайте виртуальное окружение Python и активируйте его:
    ```bash
    python -m venv venv
    source venv/bin/activate   # Для Mac/Linux
    venv\Scripts\activate      # Для Windows

3. Установите зависимости:
    ```bash
    pip install -r requirements.txt
   
4. Настройте .env файл: Скопируйте пример файла .env.example в .env:
    ```bash 
    cp .env.example .env

5. Пример содержимого .env.example:
    ```txt
    UI_BASE_URL=https://www.demoblaze.com
    API_BASE_URL=https://jsonplaceholder.typicode.com

6. Соберите Docker-образы:
    ```bash
    docker-compose build

---

## Запуск тестов

1. Запуск всех тестов:
    ```bash
    pytest -v

2. Генерация Allure-отчета:
    ```bash
    allure serve allure-results

3. Запуск нагрузочного тестирования с JMeter:
    ```bash
    docker compose up jmeter

4. Запуск остальных тестов:
    ```bash
    docker compose up tests

5. Просмотр Allure-отчетов в Docker: Перейдите по адресу http://localhost:5050.

6. Просмотр JMeter-отчетов: Перейдите по адресу http://localhost:8080.

---

## Запуск через Docker

1. Для запуска проекта через Docker нужно создать общую сеть:
    ```bash
    docker network create aqa_network

2. Запуск контейнеров:
    ```bash
    docker compose up -d --build

3. Остановка контейнеров:
    ```bash
    docker compose down

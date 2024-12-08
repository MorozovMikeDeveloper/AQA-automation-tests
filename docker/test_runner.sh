#!/bin/sh

set -e

echo "Starting test execution..."

# Запуск тестов с генерацией Allure и JUnit отчетов
echo "Running tests..."
pytest -v --junitxml=/app/allure-results/report.xml || echo "Tests failed. Continuing..."

# Генерация Allure-отчета
echo "Generating Allure report..."
allure generate /app/allure-results -o /app/allure-report --clean || echo "Failed to generate Allure report. Continuing..."

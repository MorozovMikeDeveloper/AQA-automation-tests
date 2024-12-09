#!/bin/sh

set -e

echo "Starting test execution..."

# Очистка предыдущих отчетов
echo "Cleaning up old reports..."
rm -rf /app/allure-results/* || echo "No previous results to clean"
rm -rf /app/allure-report/* || echo "No previous reports to clean"

# Запуск тестов с проверкой завершения
echo "Running tests..."
if pytest -v --junitxml=/app/allure-results/report.xml --alluredir=/app/allure-results; then
    echo "Tests completed successfully."
else
    echo "Tests failed. Generating report anyway."
fi

# Генерация Allure-отчета
echo "Generating Allure report..."
if allure generate /app/allure-results -o /app/allure-report --clean; then
    echo "Allure report generated successfully."
else
    echo "Failed to generate Allure report."
    exit 1
fi

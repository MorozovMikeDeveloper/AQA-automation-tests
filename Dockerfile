FROM python:3.11-slim

# Установим зависимости
RUN apt-get update && apt-get install -y \
    openjdk-17-jre \
    gcc \
    libpq-dev \
    curl \
    git \
    build-essential \
    libffi-dev \
    wget \
    gnupg \
    libnss3 \
    libxss1 \
    libappindicator1 \
    fonts-liberation \
    xdg-utils \
    chromium-driver \
    && apt-get clean

# Устанавливаем Chrome
RUN wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | apt-key add - \
    && echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google-chrome.list \
    && apt-get update && apt-get install -y google-chrome-stable --no-install-recommends

# Установка Allure CLI
RUN curl -o allure.tgz -L https://github.com/allure-framework/allure2/releases/download/2.32.0/allure-2.32.0.tgz \
    && tar -xzf allure.tgz -C /opt/ \
    && ln -s /opt/allure-2.32.0/bin/allure /usr/bin/allure \
    && rm allure.tgz

# Создаём рабочую директорию
WORKDIR /app

COPY requirements.txt .

# Устанавливаем Python-зависимости
RUN pip install --no-cache-dir -r requirements.txt

COPY . .


# Настройка прав доступа
RUN chmod -R 755 . && chmod a+x docker/*.sh

# Устанавливаем команду по умолчанию
CMD ["/bin/sh", "docker/test_runner.sh"]

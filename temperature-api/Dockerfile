# Используем легковесный базовый образ Python
FROM python:3.9-slim

# Установка рабочего каталога
WORKDIR /app

# Копирование файлов и установка зависимостей
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Копирование основного приложения
COPY app.py .

# Открытие порта
EXPOSE 8081

# Определение команды запуска
CMD ["python", "app.py"]
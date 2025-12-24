# Используем легковесный базовый образ Python
FROM python:3.11-slim
# Установка рабочего каталога
WORKDIR /app
# Установка зависимостей ОС
RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*
# Установка зависимостей Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

# Flask по умолчанию будет на 5000, открываем его
EXPOSE 5000

CMD ["python", "app.py"]

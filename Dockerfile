# Используем базовый образ Python
FROM python:3.11

# Установка рабочей директории
WORKDIR /app

# Копирование скрипта приложения и wait-for-it.sh
COPY app.py /app
COPY wait-for-it.sh /app

# Установка необходимых пакетов
RUN pip install psycopg2-binary

# Запуск скрипта ожидания и приложения
CMD ["./wait-for-it.sh", "db:5432", "--", "python", "app.py"]

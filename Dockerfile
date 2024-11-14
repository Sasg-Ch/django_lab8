FROM python:3.10

WORKDIR /app

RUN apt-get update \
    && apt-get install -y default-mysql-client

COPY . .

RUN pip install --no-cache-dir django gunicorn mysqlclient

EXPOSE 8000

# Команда для запуска сервера
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
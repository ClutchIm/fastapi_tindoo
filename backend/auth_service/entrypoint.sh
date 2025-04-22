#!/bin/sh
echo "Ожидание PostgreSQL..."
while ! nc -z auth_db 5432; do sleep 1; done
echo "PostgreSQL запущен."

echo "Применяем миграции..."
alembic upgrade head

sleep 2

echo "Запускаем сервер..."
exec uvicorn src.main:app --host 0.0.0.0 --port 8000 --reload
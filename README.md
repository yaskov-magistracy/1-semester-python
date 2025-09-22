# Описание
Проект по получению уведомлений на элемктронную почту

# Стек
Front:
- Next.js

Back:
- python
- fastapi
- SQLAlchemy (async)
- Alembic (Migrations)
- Pydantic (Data validation)
- dramatiq(почти)

Database:
- PostgreSQL

# Как запустить

1. Установить зависимости
`pip install -r requirements.txt`

1. Проставить свои переменные окружения в config.py

1. Запустить миграции
`alembic upgrade head`

2. Запустить бэк 
`python main.py`

1. Смотреть доку по урлу
`http://127.0.0.1:8000/docs`

1. Скачать зависимости фронта и Запустить фронт 
`npm i && npm run dev`

# Как запустить тесты

`pytests`

FROM python:3.12.0

WORKDIR /app

COPY ./backend ./backend
COPY ./api.config.json ./api.config.json

WORKDIR /app/backend

RUN pip install poetry==1.7.0
RUN poetry install

CMD poetry run alembic upgrade head; poetry run prod
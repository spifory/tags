FROM python:3.11-slim-bullseye

WORKDIR /bot

RUN pip install poetry==1.5.1

COPY pyproject.toml poetry.lock ./

RUN poetry config virtualenvs.in-project true

RUN poetry install --only=main --no-interaction --no-root

COPY . .

CMD [ "sh", "./entrypoint.sh" ]
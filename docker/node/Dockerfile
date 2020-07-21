FROM python

RUN pip install poetry

WORKDIR /app

COPY snakechain/node/pyproject.toml ./pyproject.toml

RUN poetry config virtualenvs.create false

RUN poetry install -n

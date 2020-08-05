FROM python

RUN apt-get update && apt-get install -y libprotobuf-dev protobuf-compiler
RUN pip install --upgrade pip
RUN pip install poetry

WORKDIR /app

COPY snakechain/pyproject.toml ./pyproject.toml

RUN poetry config virtualenvs.create false

RUN poetry install -n

FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

# set environment variables
ENV \
    PYTHONWRITEBYTECODE=1\
    PYTHONBUFFERED=1\
    PYTHONFAULTHANDLER=1

#Install poetry
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | POETRY_HOME=/opt/poetry python && \
    cd /usr/local/bin && \
    ln -s /opt/poetry/bin/poetry && \
    poetry config virtualenvs.create false

COPY ./pyproject.toml .

COPY ./poetry.lock* .

RUN poetry install --no-root --no-dev

COPY . .

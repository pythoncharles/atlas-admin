FROM python:3.13-slim

COPY sources.list /etc/apt/sources.list

WORKDIR /app

RUN pip install --no-cache-dir poetry==2.1.3
COPY pyproject.toml poetry.lock* ./
RUN poetry config virtualenvs.create false && poetry install --only main --no-root

COPY . .
RUN poetry install --only main

CMD ["python", "manage.py", "runserver", "0.0.0.0:9999"]

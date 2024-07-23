FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apt update && apt install --no-install-recommends -y curl build-essential
RUN pip install -U poetry --no-cache-dir && \
    poetry config virtualenvs.create false

RUN mkdir /app
WORKDIR /app

COPY pyproject.toml /app
COPY poetry.lock /app
RUN poetry install --no-root --no-cache --no-interaction

COPY . /app

EXPOSE 8001

CMD ["gunicorn", "--bind", ":8001", "--workers", "3", "--access-logfile" , "-" , "--error-logfile" , "-", "notification_service.wsgi:application"]

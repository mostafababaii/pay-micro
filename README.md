# Microservices Project

This project consists of two microservices: `auth` and `notification`. Both services are built
using Django REST Framework (DRF), PostgreSQL, Redis, RabbitMQ, and JWT for authentication.
The services are containerized using Docker and managed with Docker Compose.
Dependency management is handled using Poetry, and pre-commit hooks are used for code quality checks.

## Table of Contents

•  [Microservices](#microservices)

•  [Auth Service](#auth-service)

•  [Notification Service](#notification-service)

•  [Setup](#setup)

•  [Installation](#installation)


## Microservices

### Auth Service

The `auth` service handles user authentication and authorization. It exposes the following APIs:

•  Register User: `POST /api/users/`

•  Login: `POST /api/token/`

•  Refresh Token: `POST /api/token/refresh/`


The service runs on port `8000`.

#### Post Save Signal

After a user registers, a post-save signal is triggered,
sending the user's contact information to the `notification` service via RabbitMQ.
This is necessary because each microservice has its own database and must maintain its own data.


### Notification Service

The `notification` service handles sending OTP codes asynchronously using Celery. It exposes the following API:

•  Send OTP: `POST /api/otp/`


The service runs on port `8001`.

## Setup

### Prerequisites

•  Docker

•  Docker Compose


### Installation

```bash
git clone git@github.com:mostafababaii/pay-micro.git
cd pay-micro

Build and start the services:

Docker commands:

docker compose up -d
docker compose exec -it auth python manage.py migrate
docker compose exec -it notification python manage.py migrate

You can also use Makefile commands:

make build
make migrate-auth
make migrate-notification


Usage Services:

Auth Service Usage
Register User API:

curl -X POST http://127.0.0.1:8000/api/users/ \
-H 'Content-Type: application/json' \
-d '{
"username": "testuser",
"email": "test@mail.com",
"password": "testpassword"
}'


Login API:

curl -X POST http://127.0.0.1:8000/api/token/ \
-H 'Content-Type: application/json' \
-d '{
"username": "testuser",
"password": "testpassword"
}'


Refresh Token API:

curl -X POST http://127.0.0.1:8000/api/token/refresh/ \
-H 'Content-Type: application/json' \
-d '{
"refresh": "access-token"
}'


Notification Service Usage
Send OTP API:

curl -X POST http://127.0.0.1:8001/api/otp/ \
-H 'Content-Type: application/json' \
-H 'Authorization: Bearer access-token'

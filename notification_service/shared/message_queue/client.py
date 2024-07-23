from __future__ import annotations

from dataclasses import dataclass

import pika
from django.conf import settings


@dataclass
class RabbitMQConfig:
    host: str
    port: int
    username: str
    password: str
    virtual_host: str


def get_amq_client(config: RabbitMQConfig):
    credentials = pika.PlainCredentials(
        username=config.username, password=config.password,
    )

    connection_params = pika.ConnectionParameters(
        host=config.host,
        port=config.port,
        virtual_host=config.virtual_host,
        credentials=credentials,
    )

    return pika.BlockingConnection(connection_params)


rabbitmq_config = RabbitMQConfig(
    host=settings.RABBITMQ_HOST,
    port=settings.RABBITMQ_PORT,
    username=settings.RABBITMQ_USERNAME,
    password=settings.RABBITMQ_PASSWORD,
    virtual_host=settings.RABBITMQ_VHOST,
)

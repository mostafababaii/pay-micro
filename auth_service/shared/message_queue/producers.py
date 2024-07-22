from __future__ import annotations

from shared.message_queue import base as queue
from shared.message_queue import client as rabbit_client


def publish_user_data(data: dict):
    client = rabbit_client.get_amq_client(config=rabbit_client.rabbitmq_config)
    config = queue.RabbitMQQueueConfig(
        queue='user',
        routing_key='ur',
        exchange='amq.direct',
        durable=True,
        exclusive=False,
    )
    producer = queue.RabbitMQProducer(client, config)
    producer.publish(data)

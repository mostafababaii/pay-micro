from __future__ import annotations

from django.core.management.base import BaseCommand
from shared.message_queue import base as queue
from shared.message_queue import client as rabbit_client
from shared.message_queue import consumers


class Command(BaseCommand):
    help = 'User consumer'

    def handle(self, *args, **options):
        client = rabbit_client.get_amq_client(
            config=rabbit_client.rabbitmq_config,
        )
        config = queue.RabbitMQQueueConfig(
            queue='user',
            routing_key='ur',
            exchange='amq.direct',
            durable=True,
            exclusive=False,
        )

        consumer = consumers.UserConsumer(client, config)
        consumer.listen()

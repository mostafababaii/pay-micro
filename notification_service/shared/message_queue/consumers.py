from __future__ import annotations

import json

from django.contrib.auth import get_user_model
from shared.message_queue import base as queue

user = get_user_model()


class UserConsumer(queue.RabbitMQConsumer):
    @staticmethod
    def callback(ch, method, properties, body):
        payload = json.loads(body.decode())
        print(f"consume user with username: {payload['username']} and email: {payload['email']}")  # noqa
        user.objects.create(
            username=payload['username'],
            email=payload['email'],
            is_active=True,
        )
        ch.basic_ack(delivery_tag=method.delivery_tag)

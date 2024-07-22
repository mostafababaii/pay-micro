from __future__ import annotations

from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver
from shared.message_queue.producers import publish_user_data


@receiver(post_save, sender=get_user_model())
def send_user_data(sender, instance, created, **kwargs):
    if created:
        user_data = {
            'username': instance.username,
            'email': instance.email,
        }
        publish_user_data(user_data)

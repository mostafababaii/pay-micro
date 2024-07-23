from __future__ import annotations

from notification_service.celery import app


@app.task(name='send_otp', queue='otp', max_retries=3)
def send_otp(user_id):
    # Our logic to send OTP via provider API
    pass

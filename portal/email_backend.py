import requests
from django.conf import settings

def send_email_via_api(to_email, subject, body):
    payload = {
        "to": to_email,
        "subject": subject,
        "body": body,
        "sender": "Stream App"
    }

    response = requests.post(
        settings.EMAIL_API_URL,
        json=payload,
        timeout=getattr(settings, "EMAIL_API_TIMEOUT", 10)
    )

    response.raise_for_status()
    return response.json()

from django.core.mail.backends.base import BaseEmailBackend
import requests

class APIEmailBackend(BaseEmailBackend):
    """
    Custom email backend that sends emails via an external API.
    """
    def send_messages(self, email_messages):
        sent_count = 0
        for message in email_messages:
            data = {
                "to": message.to,
                "subject": message.subject,
                "body": message.body,
                "from": "Stream <emailsender880@gmail.com>",
            }
           
            response = requests.post(
                "https://christiangarcia.pythonanywhere.com/send",
                json=data,
                timeout=10
            )
            if response.status_code == 200:
                sent_count += 1
        return sent_count

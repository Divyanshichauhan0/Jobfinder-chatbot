from twilio.rest import Client
from config import TWILIO_SID, TWILIO_TOKEN, WHATSAPP_FROM
import os

def send_whatsapp_notification(to, jobs):
    account_sid = os.getenv('TWILIO_SID')
    auth_token = os.getenv('TWILIO_TOKEN')
    from_whatsapp = os.getenv('WHATSAPP_FROM')

    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body=f"Found {len(jobs)} matching jobs!",
        from_=f'whatsapp:{from_whatsapp}',
        to=f'whatsapp:{to}'
    )

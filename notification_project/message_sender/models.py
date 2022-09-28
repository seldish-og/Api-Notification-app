from django.db import models
from api.models import Mailing, Client


class Message(models.Model):
    CONDITION_WAIT = 'wait'
    CONDITION_SENT = 'sent'
    CONDITION_CANCELED = 'canceled'
    CONDITION_RETRY = 'retry'
    CONDITIONS = [
        (CONDITION_WAIT, 'wait'),
        (CONDITION_SENT, 'sent'),
        (CONDITION_CANCELED, 'canceled'),
        (CONDITION_RETRY, 'retry')
    ]

    condition = models.CharField(
        max_length=10, choices=CONDITIONS, default=CONDITION_WAIT,)
    sent_time = models.DateTimeField(auto_now_add=True, blank=True)
    mailing = models.ForeignKey(
        Mailing, on_delete=models.CASCADE, related_name='mailing')
    client = models.ForeignKey(
        Client, on_delete=models.CASCADE, related_name='client')

import os
import requests
from celery import shared_task
from api.models import Mailing, Client
from api.serializers import MailingSerializer

from django.db.models import Q
from celery.schedules import crontab
from notification_project.celery import app


URL = os.getenv("URL")
TOKEN = os.getenv("TOKEN")


def test_print(a):
    print(a)


def get_clients(clients_filter):
    clients = Client.objects.filter(
        Q(mobile_operator_code=clients_filter) |
        Q(client_timezone=clients_filter) |
        Q(tag=clients_filter)
    )
    return clients


def send_message(client, message, message_id, url=URL, token=TOKEN):
    url = URL + str(message_id)
    try:
        requests.post(url)
        return 200
    except requests.RequestException as ex:
        return ex


@shared_task
def start_mailing(mailing):
    client_filter = mailing["client_properties_filter"]
    test_print(client_filter)

    clients = get_clients(clients_filter=client_filter)
    test_print(clients)

    return mailing[0]


# @app.on_after_configure.connect
# def setup_mailing(sender, **kwargs):
#     # Executes every Monday morning at 7:30 a.m.
#     sender.add_periodic_task(
#         crontab(hour=7, minute=30, day_of_week=1),
#         start_mailing.s('Happy Mondays!'),
#     )

# {'id': 1, 'date_start': '2022-09-15 11:56', 'date_end': '2022-09-15 11:56', 'message': 'Hello visit us)', 'client_properties_filter': '+7'}

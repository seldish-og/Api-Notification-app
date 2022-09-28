from django.db import models
from datetime import datetime
from django.utils import timezone


class Client(models.Model):
    phone_number = models.CharField(max_length=11)
    mobile_operator_code = models.IntegerField()
    tag = models.CharField(max_length=100,  blank=True)
    client_timezone = models.CharField(max_length=10, default="UTC")


class Mailing(models.Model):
    date_start = models.DateTimeField(auto_now_add=True, blank=True)
    date_end = models.DateTimeField(auto_now_add=True, blank=True)
    message = models.TextField(max_length=400)
    client_properties_filter = models.CharField(max_length=64)


# {
#     "date_start": "",
#     "date_end": "",
#     "message": "Hello visit us)",
#     "client_properties_filter": "+7"

# }
# {
#     "phone_number": "79408349023",
#     "mobile_operator_code": "+7",
#     "tag": "user4",
#     "client_timezone": "UTC+1"
# }

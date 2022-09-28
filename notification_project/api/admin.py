from django.contrib import admin

from .models import Mailing, Client


admin.site.register(Mailing)
admin.site.register(Client)

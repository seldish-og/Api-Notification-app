from django.urls import path
from . import views

urlpatterns = [
    path('get_statistics', views.StatisticsView.as_view()),
]

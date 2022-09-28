from django.urls import path
from . import views

urlpatterns = [
    path('get_all_clients', views.ClientView.as_view()),
    path('add_client', views.ClientView.as_view()),
    path('update_client/<int:client_id>/', views.ClientView.as_view()),
    path('delete_client/<int:client_id>/', views.ClientView.as_view()),

    path('get_all_mailing', views.MailingView.as_view()),
    path('add_mailing', views.MailingView.as_view()),
    path('update_mailing/<int:mailing_id>/', views.MailingView.as_view()),
    path('delete_mailing/<int:mailing_id>/', views.MailingView.as_view()),


]

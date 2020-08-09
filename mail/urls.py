from .views import *
from django.urls import path

urlpatterns = [
    path('', index, name='home'),
    path('list/', mails_list, name='mails')
]
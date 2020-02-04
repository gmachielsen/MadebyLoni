from django.urls import path
from . import views

app_name='contact'

urlpatterns = [
    path('MadebyLoni', views.contact, name='contact'),
]

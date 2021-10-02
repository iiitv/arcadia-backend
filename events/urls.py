from django.urls import path
from .views import  EventApi

urlpatterns = [
    path("events/", EventApi, name="events"),
]
from django.db import models
from authentication.models import User


class Event(models.Model):
    name = models.CharField(max_length = 255, null = False)
    start_date = models.DateTimeField(null = False)
    end_date = models.DateTimeField(null = False)


class Organizer(models.Model):
    event = models.ForeignKey(Event, on_delete = models.CASCADE, related_name = "event_organizer")
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name = "organizer_user")

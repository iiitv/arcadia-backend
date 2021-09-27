from django.db import models

class Event(models.Model):
    name = models.CharField(max_length=255, null=False)
    start_date = models.DateTimeField(null=False)
    end_date = models.DateTimeField(null=False)

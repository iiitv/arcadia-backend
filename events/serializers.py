from rest_framework.serializers import ModelSerializer
from .models import Event, Organizer


class EventSerializer(ModelSerializer):
    class Meta:
        model = Event
        fields = "__all__"


class OrganizerSerializer(ModelSerializer):
    class Meta:
        model = Organizer
        fields = "__all__"

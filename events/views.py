from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .serializers import EventSerializer, OrganizerSerializer
from .models import Event, Organizer
from .permissions import SafeMethodPermission


class EventApi(ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated, SafeMethodPermission]


class OrganizerApi(ModelViewSet):
    queryset = Organizer.objects.all()
    serializer_class = OrganizerSerializer
    permission_classes = [IsAuthenticated, SafeMethodPermission]

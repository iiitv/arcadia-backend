from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .serializers import EventSerializer
from .models import Event


class EventApi(ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        if request.user.is_staff or request.user.is_superuser:
            return super().create(request, *args, **kwargs) 
        else:
            return Response({"status": "User unauthorized"}, status=status.HTTP_401) 

    def update(self, request, *args, **kwargs):
        if request.user.is_staff or request.user.is_superuser:
            return super().update(request, *args, **kwargs)
        else:
            return Response({"status": "User unauthorized"}, status=status.HTTP_401) 


    def partial_update(self, request, *args, **kwargs):
        if request.user.is_staff or request.user.is_superuser:
            return super().partial_update(request, *args, **kwargs)
        else:
            return Response({"status": "User unauthorized"}, status=status.HTTP_401) 

    def destroy(self, request, *args, **kwargs):
        if request.user.is_staff or request.user.is_superuser:
            return super().destroy(request, *args, **kwargs)
        else:
            return Response({"status": "User unauthorized"}, status=status.HTTP_401) 

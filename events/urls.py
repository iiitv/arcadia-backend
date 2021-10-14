from django.urls import path
from .views import EventApi, OrganizerApi
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'events', EventApi)
router.register(r'organizers', OrganizerApi)

urlpatterns = router.urls

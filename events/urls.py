from django.urls import path
from .views import EventApi
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'events', EventApi)

urlpatterns = router.urls

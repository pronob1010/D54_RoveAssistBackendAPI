from django.urls import path
from rest_framework import routers
from rest_framework.routers import DefaultRouter

from. views import *

router = DefaultRouter()
router.register("place", addPlaceViewSet, basename="place"),
router.register("packagetour", packageTourViewSet, basename="packagetour"),

urlpatterns = [
    
] + router.urls

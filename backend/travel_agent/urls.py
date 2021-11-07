from django.urls import path
from rest_framework import routers
from rest_framework.routers import DefaultRouter

from. views import *

router = DefaultRouter()
router.register("agentlist", agentViewSet, basename="agentlist"),
router.register("companylist", CompanyInfoViewSet, basename="companylist"),
router.register("hotellist", hotelViewSet, basename="hotellist"),
router.register("roomlist", roomViewSet, basename="roomlist"),


urlpatterns = [
    
] + router.urls

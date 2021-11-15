from django.shortcuts import render
from rest_framework import serializers
from rest_framework.viewsets import ModelViewSet

from . models import *
from . serializers import *
from rest_framework.response import Response

class addPlaceViewSet(ModelViewSet):
    serializer_class = addPlaceSerializer
    queryset = addPlace.objects.all()

class addRestaurantViewSet(ModelViewSet):
    serializer_class = addRestaurantSerializer
    queryset = addRestaurant.objects.all()

class packageTourViewSet(ModelViewSet):
    serializer_class = packageTourSerializer
    queryset = packageTour.objects.all()
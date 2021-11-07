from django.shortcuts import render
from rest_framework import serializers
from rest_framework.viewsets import ModelViewSet

from . models import *
from . serializers import *
from rest_framework.response import Response

class agentViewSet(ModelViewSet):
    serializer_class = agentSerializer
    queryset = agent.objects.all()

class CompanyInfoViewSet(ModelViewSet):
    serializer_class = CompanyInfoSerializer
    queryset = CompanyInfo.objects.all()

class hotelViewSet(ModelViewSet):
    serializer_class = hotelSerializer
    queryset = Hotel.objects.all()

class roomViewSet(ModelViewSet):
    serializer_class = RoomSerializer
    queryset = room.objects.all()
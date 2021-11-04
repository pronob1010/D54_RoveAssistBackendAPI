from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

# Create your views here.
from.serializers import *
from.models import *
class notesViewSet(ModelViewSet):
    serializer_class = noteSerializer
    queryset =  note.objects.all()
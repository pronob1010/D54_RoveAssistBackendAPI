from django.db.models import fields
from rest_framework.serializers import ModelSerializer

from.models import *

class addPlaceSerializer(ModelSerializer):
    class Meta:
        model = addPlace
        fields = '__all__'

class packageTourSerializer(ModelSerializer):
    class Meta:
        model = packageTour
        fields = '__all__'

class addRestaurantSerializer(ModelSerializer):
    class Meta:
        model = addRestaurant
        fields = '__all__'


from django.db.models import fields
from rest_framework.serializers import ModelSerializer

from.models import *

class CompanyInfoSerializer(ModelSerializer):
    class Meta:
        model = CompanyInfo
        fields = "__all__"

class agentSerializer(ModelSerializer):
    company_info = CompanyInfoSerializer(source = "company_root")
    class Meta:
        model = agent
        fields = '__all__'

class roomSerializer(ModelSerializer):
    class Meta:
        model = room
        fields = "__all__"

class hotelSerializer(ModelSerializer):
    # room_list = roomSerializer(source = "root_hotels")
    class Meta:
        model = companyHotel
        fields = '__all__'

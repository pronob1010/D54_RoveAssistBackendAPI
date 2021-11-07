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

# class roomSerializer(ModelSerializer):
#     class Meta:
#         model = room
#         # fields = ['rel_hotel','title','image','type',]
#         # fields = ['title','image','type',]
#         fields = "__all__"
#         # fields = ['rel_hotel','title','image','type','facilities','quantity', 'price', 'booked_by']


class RoomSerializer(ModelSerializer):
    class Meta:
        model = room
        fields = "__all__"
class hotelSerializer(ModelSerializer):
    room_list = RoomSerializer(source = "root_hotels",many = True, read_only = True)
    class Meta:
        model = Hotel
        fields = '__all__' 

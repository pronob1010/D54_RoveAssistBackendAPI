from rest_framework.authentication import TokenAuthentication
from rest_framework.viewsets import ModelViewSet
from . models import *
from . serializers import *
from rest_framework.response import Response
from . import permissions



class UserViewSet(ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    # authentication_classes = (TokenAuthentication,)
    # permission_classes = (permissions.UpdateOwnUser,)

    # def update(self, request, *args, **kwargs):
    #     user = self.get_object()
    #     data = request.data
        
    #     user.firstname = data['firstname']
    #     user.lastname =  data['lastname']
         
    #     user.phone = data['phone']
    #     user.home_address = data['home_address']
    #     user.save()
    #     serializer = UserSerializer(user)
    #     return Response(serializer.data)




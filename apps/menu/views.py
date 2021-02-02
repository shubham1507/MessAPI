from rest_framework import viewsets
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication
from .models import Menu
from .serializers import *
from apps.accounts.permissions import *

class MenuListing(viewsets.ModelViewSet):
    permission_classes=[IsAuthenticated]
    authentication_classes=[SessionAuthentication]
    serializer_class = MenuOfTheDaySerializer
    queryset = Menu.objects.all()

    # def get_permissions(self):
    #     user = self.request.user 
    #     permission_classes=[]
    #     if self.action=='retrive' or self.action=='create':
    #         permission_classes=[IsAuthenticated]
    #     return [permission() for permission in permission_classes]
        
    def perform_create(self,serializer):
        serializer.save(vendor=self.request.user)
    

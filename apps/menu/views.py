from rest_framework import viewsets
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication
from .models import Menu
from .serializers import *
from apps.accounts.permissions import *

class MenuListing(viewsets.ModelViewSet):
    # permission_classes=[IsAuthenticated]
    serializer_class = MenuOfTheDaySerializer
    queryset = Menu.objects.all()

    def perform_create(self,serializer):
        serializer.save(vendor=self.request.user)

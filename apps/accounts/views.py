from rest_framework.authtoken.models import Token

from django.http import JsonResponse
from rest_framework import viewsets
from rest_framework.authtoken.views import ObtainAuthToken

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import mixins, viewsets

from .models import *
from .serializers import *
from .permissions import *
from django.views.decorators.csrf import csrf_exempt

from django.contrib.auth import get_user_model

UserModel = get_user_model()
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        user = self.request.user
        permission_classes = []
        if self.action == 'create':
            permission_classes = [AllowAny]
        elif self.action == 'retrieve' or self.action == 'update' or self.action == 'partial_update':
            permission_classes = [IsLoggedInUserOrAdmin,IsAuthenticated]
        elif self.action == 'list' or self.action == 'destroy':
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]

class ForgotPassword(APIView):
    def post(self,request,format=None):
        serializer = ForgotPasswordSerializer(data=request.data)
        if serializer.is_valid():
            email= request.data["email"]
            try:
                user = UserModel.objects.get(email = email)
                otp = 12345    
                token, created = Token.objects.get_or_create(user=user)

                return Response({"otp":token.key})
            except UserModel.DoesNotExist:
                return Response({'error':'Invalid email address'})
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        




class ChangePasswordView(generics.UpdateAPIView):

    queryset = User.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = ChangePasswordSerializer



class VendorListing(mixins.ListModelMixin, viewsets.GenericViewSet):

    model = User
    serializer_class = VendorListSeializer

    def get_queryset(self):

        queryset = User.objects.filter(is_seller=True)

        return queryset

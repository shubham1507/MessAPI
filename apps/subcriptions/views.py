from django.contrib import auth
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.views import APIView
from .serializers import SubscriptionSerializer,CustSubscriptionSerializer
from .models import Subscription,CustomerSubscription
from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

UserModel = get_user_model()

# Create your views here.

def get_instance(request):
    user = UserModel.objects.get(id=request.user.id)
    return user

class Service(viewsets.ModelViewSet):
    
    permission_classes=[IsAuthenticated]
    authentication_classes=[SessionAuthentication]
    serializer_class = SubscriptionSerializer
    queryset = Subscription.objects.all()


    def perform_create(self,serializer):
        user = get_instance(self.request)
        print(user.username)
        serializer.save(vendor=user)


class CustomerSubscriptionView(APIView):
    permission_classes=[IsAuthenticated]
    authentication_classes=[SessionAuthentication]
    

    def get(self,request,sub_id):
        user = get_instance(self.request)
        custsub = CustomerSubscription.objects.filter(subscription__id=sub_id,customer=user)
        serializer = CustSubscriptionSerializer(custsub,many=True)
        user = self.request.user
        print("User is ",user.id)
        return Response(serializer.data)
    def post(self,request,sub_id):
        serializer =CustSubscriptionSerializer(data = request.data) 
        print("User is " ,self.request.user)

        if serializer.is_valid(raise_exception=True):
            user = UserModel.objects.get(id = self.request.user.id)
            sub = Subscription.objects.filter(id=sub_id)
            print(sub)
            serializer.save(subscription=sub,customer = user)
            return Response(serializer.data)
        return Response(serializer.error)
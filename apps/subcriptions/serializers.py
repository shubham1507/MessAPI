from rest_framework import serializers
from .models import Subscription,CustomerSubscription


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:

        model = Subscription
        fields = ('subscription_type','subscription_menu','price')

class CustSubscriptionSerializer(serializers.ModelSerializer):
    subscription = SubscriptionSerializer(many=True,required=True)
    class Meta:
        model = CustomerSubscription
        fields = ('transaction_id','payment_mode',"subscription")
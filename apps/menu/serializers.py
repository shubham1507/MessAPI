from rest_framework import serializers
from .models import Menu


class MenuOfTheDaySerializer(serializers.ModelSerializer):
    class Meta:

        model = Menu
        fields = ('date','meal_type','menu')
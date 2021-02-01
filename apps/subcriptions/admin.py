from django.contrib import admin
from .models import Subscription, CustomerSubscription
# Register your models here.


@admin.register(Subscription, CustomerSubscription)
class AppAdmin(admin.ModelAdmin):
    pass

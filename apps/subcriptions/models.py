from django.db import models
from apps.accounts.models import User, Vendor, Customer
from apps.menu.models import MENU_CHOICES
import uuid


# Create your models here.
class Subscription(models.Model):

    SUB_PLAN = (
        ('M', 'MONTHLY'),
        ('W', 'WEEKLY'),
        ('D', 'ONE TIME'),
        ('F', 'FULL MEAL'),
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    subscription_type = models.CharField('SUB_PLAN',
                                         choices=SUB_PLAN,
                                         max_length=20)
    subscription_menu = models.CharField(choices=MENU_CHOICES, max_length=20)
    price = models.PositiveIntegerField()

    def __str__(self):
        return 'Subscription by: {}'.format(self.vendor)


class CustomerSubscription(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    subscription = models.OneToOneField(
        Subscription, on_delete=models.CASCADE, default=None)
    transaction_id = models.CharField(max_length=100)
    payment_mode = models.CharField(max_length=100)
    isPaid = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return ' {}'.format(self.customer)

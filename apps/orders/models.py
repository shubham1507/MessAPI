from django.db import models
from apps.menu.models import Menu
from apps.accounts.models import User
# from apps.subscriptions.models import CustomerSubscription

# from apps.subcriptions.models import CustomerSubscription
import uuid

# Create your models here.


class Order(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    # user_subscription = models.ForeignKey(CustomerSubscription,
    #                                       on_delete=models.CASCADE)
    is_cancelled = models.BooleanField(default=False)
    order_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return 'menu order: {}'.format(self.menu)
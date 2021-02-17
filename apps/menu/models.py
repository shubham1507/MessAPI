from django.db import models
from apps.accounts.models import User, Vendor
import uuid


# Create your models here.
MENU_CHOICES = (('Break fast', 'Break fast'), ('Lunch', 'Lunch'), ('Dinner',
                                                                   'Dinner'))


class Menu(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)

    date = models.DateField(null=True, blank=True)
    meal_type = models.CharField(choices=MENU_CHOICES, max_length=50)
    menu = models.TextField()

    def __str__(self):
        return 'Mealtype By: {}'.format(self.vendor.user.username)

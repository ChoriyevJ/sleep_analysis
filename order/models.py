from django.db import models
from django.contrib.auth import get_user_model

from shop.models import Product
from utils.models import BaseModel


User = get_user_model()


class Address(BaseModel):

    class Status(models.TextChoices):
        DELIVERED = "DELIVERED"
        ONGOING = "ONGOING"
        CANCELLED = "CANCELLED"

    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='addresses')
    full_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    landmark = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    pincode = models.CharField(max_length=255)
    contact_number = models.CharField(max_length=15)
    status = models.CharField(max_length=15, choices=Status.choices, default=Status.DELIVERED)
    paid = models.BooleanField(default=False)


class Coupon(BaseModel):
    code = models.CharField(max_length=255)
    discount = models.DecimalField(max_digits=5, decimal_places=1)
    finish_date = models.DateField()
    finish_time = models.TimeField()
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.code


class Order(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='orders')
    address = models.ForeignKey(Address, on_delete=models.SET_NULL,
                                related_name='orders', blank=True, null=True)

    quantity = models.PositiveIntegerField()
    amount = models.DecimalField(max_digits=10, decimal_places=1)





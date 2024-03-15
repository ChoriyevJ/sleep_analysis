from django.db import models
from django.contrib.auth import get_user_model

from utils.models import BaseModel


User = get_user_model()


class Order(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='orders')
    full_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    landmark = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    pincode = models.CharField(max_length=255)
    contact_number = models.CharField(max_length=15)






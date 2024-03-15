from decimal import Decimal

from django.db import models
from django.utils.text import slugify

from utils.models import BaseModel
from django.contrib.auth import get_user_model

User = get_user_model()


class Category(BaseModel):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, blank=True, null=True,
                            unique=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Brand(BaseModel):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, blank=True, null=True,
                            unique=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Product(BaseModel):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, blank=True, null=True,
                            unique=True)
    description = models.TextField()

    image = models.ImageField(upload_to='product/image/',
                              blank=True, null=True)
    price = models.PositiveSmallIntegerField()
    quantity = models.PositiveIntegerField()
    rating = models.FloatField(blank=True, null=True)

    category = models.ForeignKey(Category, on_delete=models.CASCADE,
                                 related_name='products')
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE,
                              related_name='products')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Rating(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE,
                                related_name='ratings')
    profile = models.ForeignKey('users.Profile', on_delete=models.CASCADE,
                                related_name="ratings")
    rating = models.PositiveSmallIntegerField(default=0)


class Image(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE,
                                related_name='images')
    image = models.ImageField(upload_to='images/product/')


class Cart(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='carts')
    product = models.ForeignKey(Product, on_delete=models.CASCADE,
                                related_name='carts')
    quantity = models.PositiveSmallIntegerField(default=0)

    objects = models.Manager()

    class Meta:
        unique_together = ('user', 'product')

    @property
    def get_total_price(self):
        return self.quantity * self.product.price

    def __str__(self):
        return f'Cart(pk={self.pk})'


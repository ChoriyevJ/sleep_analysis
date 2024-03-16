from rest_framework import generics
from django.db import models

from order.models import Address, Order
from order import serializers
from shop.models import Cart


class AddressListCreateAPI(generics.ListCreateAPIView):
    queryset = Address.objects.all()
    serializer_class = serializers.AddressSerializer

    def get_queryset(self):
        return super().get_queryset().filter(
            user=self.request.user
        )

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class AddressAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Address.objects.all()
    serializer_class = serializers.AddressSerializer

    def get_queryset(self):
        return super().get_queryset().filter(
            user=self.request.user
        )


class OrderCreateAPI(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = serializers.OrderSerializer

    def perform_create(self, serializer):
        carts = Cart.objects.filter(
            user=self.request.user
        ).aggregate(
            total_price=models.Sum('get_cost'),
            quantity=models.Sum('quantity')
        )

        serializer.save(
            quantity=carts['quantity'],
            total_price=carts['total_price']
        )


class OrderAPI(generics.RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = serializers.OrderSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(
            user=self.request.user
        )




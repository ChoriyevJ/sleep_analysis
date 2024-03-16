from django.db import models
from rest_framework import generics

from order.models import Order
from shop.models import Product, Cart
from shop import serializers


class ProductListAPI(generics.ListAPIView):
    queryset = Product.objects.all().select_related(
        "category", "brand"
    ).prefetch_related("carts")
    serializer_class = serializers.ProductListSerializer


class ProductDetailAPI(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = serializers.ProductDetailSerializer


class CartAPI(generics.ListAPIView):
    queryset = Cart.objects.all()
    serializer_class = serializers.CartSerializer


class CartCreateAPI(generics.CreateAPIView):
    queryset = Cart.objects.all()
    serializer_class = serializers.CartCreateSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CartDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cart.objects.all()
    serializer_class = serializers.CartCreateSerializer





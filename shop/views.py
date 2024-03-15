from django.db import models
from rest_framework import generics


from shop.models import Product, Cart
from shop import serializers


class ProductListAPI(generics.ListAPIView):
    queryset = Product.objects.all().select_related(
        "category", "brand"
    ).prefetch_related("carts")
    serializer_class = serializers.ProductListSerializer


class ProductDetailAPI(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = serializers.ProductListSerializer


class CartAPI(generics.ListAPIView):
    queryset = Cart.objects.all()
    serializer_class = serializers.CartSerializer


class CartCreateAPI(generics.CreateAPIView):
    queryset = Cart.objects.all()
    serializer_class = serializers.CartCreateSerializer

    def perform_create(self, serializer):
        serializer.save(profile=self.request.user.profile)


class CartUpdateAPI(generics.UpdateAPIView):
    queryset = Cart.objects.all()
    serializer_class = serializers.CartCreateSerializer


class CartDeleteAPI(generics.DestroyAPIView):
    queryset = Cart.objects.all()
    serializer_class = serializers.CartCreateSerializer


class CheckOutAPI(generics.ListAPIView):
    queryset = Cart.objects.all()
    serializer_class = serializers

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(
            user=self.request.user
        )



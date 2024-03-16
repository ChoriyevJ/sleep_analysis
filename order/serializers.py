from rest_framework import serializers

from order.models import Order, Address


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = (
            'full_name',
            'address',
            'landmark',
            'city',
            'pincode',
            'contact_number',
        )


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = (
            'quantity',
            'amount',
            'shipping_fee',
        )


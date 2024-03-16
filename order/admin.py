from django.contrib import admin

from order.models import Address, Order,Coupon


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    pass


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    pass


@admin.register(Coupon)
class CouponAdmin(admin.ModelAdmin):
    pass

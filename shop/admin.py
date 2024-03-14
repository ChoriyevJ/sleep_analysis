from django.contrib import admin

from shop import models


class ImageInline(admin.StackedInline):
    model = models.Image
    extra = 0


class RatingInline(admin.StackedInline):
    model = models.Rating
    extra = 0


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


@admin.register(models.Brand)
class BrandAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ImageInline, RatingInline]
    prepopulated_fields = {'slug': ('title',)}



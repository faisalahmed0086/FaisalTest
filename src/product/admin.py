from django.contrib import admin
from .models import Product, Variant, ProductImage, ProductVariant, ProductVariantPrice

# Register your models here.
admin.site.register(Product)
admin.site.register(Variant)

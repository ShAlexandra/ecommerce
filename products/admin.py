from django.contrib import admin
from .models import Product, Category, Image


admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Image)
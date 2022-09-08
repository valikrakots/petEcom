from django.contrib import admin
from .models import Product, Image, PageImage, FavouriteItems

# Register your models here.

admin.site.register(Product)
admin.site.register(Image)
admin.site.register(PageImage)
admin.site.register(FavouriteItems)
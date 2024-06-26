from django.contrib import admin
from .models import Product, Category, ProductWishlist

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'discounted_price', 'stock', 'available', 'created_at']
    prepopulated_fields = {'slug': ('title',)}

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(ProductWishlist)
class ProductWishlistAdmin(admin.ModelAdmin):
    list_display = ['user', 'product', 'added_at']

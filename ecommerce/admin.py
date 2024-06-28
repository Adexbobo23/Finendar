from django.contrib import admin
from .models import ( 
    Product, Category, 
    ProductWishlist, ProductCartItem, 
    ProductPurchase, Tag
)

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

@admin.register(ProductCartItem)
class ProductCartItemAdmin(admin.ModelAdmin):
    list_display = ['user', 'product', 'quantity', 'added_at']

@admin.register(ProductPurchase)
class ProductPurchaseAdmin(admin.ModelAdmin):
    list_display = ['user', 'product', 'purchase_date']

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name']
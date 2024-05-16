from django.urls import path
from .views import shop, product_details, cart, checkout, wishlist

urlpatterns = [
    path('shop/', shop, name='shop'),
    path('product_details/', product_details, name='product_details'),
    path('cart/', cart, name='cart'),
    path('checkout/', checkout, name='checkout'),
    path('wishlist/', wishlist, name='wishlist'),
]
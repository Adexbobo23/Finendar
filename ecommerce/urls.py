from django.urls import path
from .views import ( 
    shop, product_details, 
    cart, checkout, wishlist, 
    add_product, add_to_wishlist, category_details
)

urlpatterns = [
    path('products/', shop, name='shop'),
    path('product/<slug:slug>/', product_details, name='product_detail'),
    path('cart/', cart, name='cart'),
    path('checkout/', checkout, name='checkout'),
    path('wishlist/', wishlist, name='wishlist'),
    path('add-product/', add_product, name='add_product'),
    path('add-to-wishlist/<int:product_id>/', add_to_wishlist, name='add_to_wishlist'),
    path('shop/categories/<slug:slug>/', category_details, name='category_details'),
]
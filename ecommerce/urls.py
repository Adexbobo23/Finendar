from django.urls import path
from .views import ( 
    shop, product_details, 
    cart, checkout, wishlist, 
    add_product, add_to_wishlist, category_details,
    product_cart, add_product_to_cart, purchase_product,
    add_product_to_cart_second
)

urlpatterns = [
    path('products/', shop, name='shop'),
    path('product/<slug:slug>/', product_details, name='product_detail'),
    path('cart/', cart, name='cart'),
    path('prduct-cart/', product_cart, name='product_cart'),
    path('checkout/', checkout, name='checkout'),
    path('wishlist/', wishlist, name='wishlist'),
    path('add-product/', add_product, name='add_product'),
    path('add_to_wishlist/<int:product_id>/', add_to_wishlist, name='add_to_wishlist'),
    path('shop/categories/<slug:slug>/', category_details, name='category_details'),
    path('add-to-cart/<int:product_id>/', add_product_to_cart, name='add_product_to_cart'),
    path('add-to-cart_second/<int:product_id>/', add_product_to_cart_second, name='add_product_to_cart_second'),
    path('purchase-product/<int:product_id>/', purchase_product, name='purchase_product'),
]
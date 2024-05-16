from django.shortcuts import render

def shop(request):
    return render(request, 'ecommerce/shop.html')

def product_details(request):
    return render(request, 'ecommerce/product-details.html')

def cart(request):
    return render(request, 'ecommerce/cart.html')

def checkout(request):
    return render(request, 'ecommerce/checkout.html')

def wishlist(request):
    return render(request, 'ecommerce/wishlist.html')
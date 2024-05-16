from django.shortcuts import render
from courses.models import CartItem
from django.contrib.auth.decorators import login_required

def shop(request):
    return render(request, 'ecommerce/shop.html')

def product_details(request):
    return render(request, 'ecommerce/product-details.html')
    
@login_required(login_url='login')
def cart(request):
    cart_items = CartItem.objects.filter(user=request.user)

    context = {
        'cart_items': cart_items,
    }
    return render(request, 'ecommerce/cart.html', context)

def checkout(request):
    return render(request, 'ecommerce/checkout.html')

def wishlist(request):
    return render(request, 'ecommerce/wishlist.html')
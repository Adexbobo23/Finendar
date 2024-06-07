from django.shortcuts import render, redirect, get_object_or_404
from courses.models import CartItem
from django.contrib.auth.decorators import login_required

def shop(request):
    return render(request, 'ecommerce/shop.html')

def product_details(request):
    return render(request, 'ecommerce/product-details.html')
    
@login_required(login_url='login')
def cart(request):
    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'clear':
            CartItem.objects.filter(user=request.user).delete()
    elif request.method == 'GET':
        cart_item_id = request.GET.get('remove')
        if cart_item_id:
            cart_item = get_object_or_404(CartItem, id=cart_item_id, user=request.user)
            cart_item.delete()
            return redirect('cart')

    cart_items = CartItem.objects.filter(user=request.user)
    context = {
        'cart_items': cart_items,
    }
    return render(request, 'ecommerce/cart.html', context)

def checkout(request):
    return render(request, 'ecommerce/checkout.html')

def wishlist(request):
    return render(request, 'ecommerce/wishlist.html')
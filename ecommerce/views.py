from django.shortcuts import render, redirect, get_object_or_404
from courses.models import CartItem
from django.contrib.auth.decorators import login_required
from .models import Product, Category, ProductWishlist
from .forms import ProductForm

def shop(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    return render(request, 'ecommerce/shop.html', {'products': products, 'categories': categories})

def product_details(request, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(request, 'ecommerce/product-details.html', {'product': product})
    
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

@login_required
def add_to_wishlist(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    Wishlist.objects.get_or_create(user=request.user, product=product)
    return redirect('wishlist')

@login_required
def wishlist(request):
    wishlist_items = Wishlist.objects.filter(user=request.user)
    return render(request, 'ecommerce/wishlist.html', {'wishlist_items': wishlist_items})

@login_required
def add_product(request):
    if request.method == 'POST':
        product_form = ProductForm(request.POST, request.FILES)
        if product_form.is_valid():
            product = product_form.save(commit=False)
            product.user = request.user
            product.save()
            return redirect('shop')
    else:
        product_form = ProductForm()
    
    return render(request, 'ecommerce/addProducts.html', {
        'product_form': product_form,
    })

def category_details(request, slug):
    category = get_object_or_404(Category, slug=slug)
    products = Product.objects.filter(category=category)
    return render(request, 'ecommerce/category_details.html', {'category': category, 'products': products})
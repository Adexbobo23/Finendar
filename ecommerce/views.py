from django.shortcuts import render, redirect, get_object_or_404
from courses.models import CartItem
from django.contrib.auth.decorators import login_required
from .models import Product, Category, ProductWishlist, ProductCartItem, ProductPurchase, ProductWishlist
from .forms import ProductForm
from django.contrib import messages
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q


@login_required(login_url='login')
def shop(request):
    query = request.GET.get('q')
    page = request.GET.get('page', 1)
    product_id = request.GET.get('product_id')
    
    if query:
        products = Product.objects.filter(
            Q(title__icontains=query) |
            Q(description__icontains=query) |
            Q(tags__name__icontains=query)
        ).distinct()
    else:
        products = Product.objects.all()
    
    paginator = Paginator(products, 9)  
    try:
        products_paginated = paginator.page(page)
    except PageNotAnInteger:
        products_paginated = paginator.page(1)
    except EmptyPage:
        products_paginated = paginator.page(paginator.num_pages)
    
    selected_product = None
    if product_id:
        selected_product = get_object_or_404(Product, id=product_id)
    
    user_wishlist = []
    if request.user.is_authenticated:
        user_wishlist = ProductWishlist.objects.filter(user=request.user).values_list('product_id', flat=True)
    
    # Calculate the range of displayed products
    start_index = (products_paginated.number - 1) * paginator.per_page + 1
    end_index = start_index + len(products_paginated.object_list) - 1

    return render(request, 'ecommerce/shop.html', {
        'products': products_paginated,
        'categories': Category.objects.all(),
        'selected_product': selected_product,
        'query': query,
        'paginator': paginator,
        'user_wishlist': user_wishlist,
        'start_index': start_index,
        'end_index': end_index,
        'total_products': paginator.count
    })




@login_required(login_url='login')
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


@login_required(login_url='login')
def product_cart(request):
    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'clear':
            ProductCartItem.objects.filter(user=request.user).delete()
    elif request.method == 'GET':
        cart_item_id = request.GET.get('remove')
        if cart_item_id:
            cart_item = get_object_or_404(ProductCartItem, id=cart_item_id, user=request.user)
            cart_item.delete()
            return redirect('cart')

    cart_items = ProductCartItem.objects.filter(user=request.user)
    context = {
        'cart_items': cart_items,
    }
    return render(request, 'ecommerce/product-cart.html', context)


@login_required(login_url='login')
def add_product_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart_item, created = ProductCartItem.objects.get_or_create(
        user=request.user,
        product=product,
    )

    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('product_detail', slug=product.slug)

@login_required(login_url='login')
def add_product_to_cart_second(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart_item, created = ProductCartItem.objects.get_or_create(
        user=request.user,
        product=product,
    )

    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('shop')


@login_required(login_url='login')
def purchase_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    # Check if the user has already purchased the product
    if ProductPurchase.objects.filter(user=request.user, product=product).exists():
        messages.warning(request, 'You have already purchased this product.')
    else:
        # Record the product purchase for the user
        ProductPurchase.objects.create(user=request.user, product=product)
        messages.success(request, 'You have successfully purchased the product.')
    
    # Redirect to the "my-products" page after purchase
    return redirect('my-products')


@login_required(login_url='login')
def checkout(request):
    return render(request, 'ecommerce/checkout.html')

@login_required(login_url='login')
def add_to_wishlist(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    ProductWishlist.objects.get_or_create(user=request.user, product=product)
    return redirect('shop')


@login_required(login_url='login')
def wishlist(request):
    wishlist_items = ProductWishlist.objects.filter(user=request.user)
    return render(request, 'ecommerce/wishlist.html', {'wishlist_items': wishlist_items})


@login_required(login_url='login')
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


@login_required(login_url='login')
def category_details(request, slug):
    category = get_object_or_404(Category, slug=slug)
    query = request.GET.get('q')
    product_id = request.GET.get('product_id')
    
    products = Product.objects.filter(category=category)
    
    if query:
        products = products.filter(
            Q(title__icontains=query) |
            Q(description__icontains=query) |
            Q(tags__name__icontains=query)
        ).distinct()
    
    paginator = Paginator(products, 9)
    page = request.GET.get('page')
    
    try:
        products_paginated = paginator.page(page)
    except PageNotAnInteger:
        products_paginated = paginator.page(1)
    except EmptyPage:
        products_paginated = paginator.page(paginator.num_pages)
    
    user_wishlist = []
    if request.user.is_authenticated:
        user_wishlist = ProductWishlist.objects.filter(user=request.user).values_list('product_id', flat=True)
    
    context = {
        'category': category,
        'products': products_paginated,
        'query': query,
        'paginator': paginator,
        'user_wishlist': user_wishlist,
    }
    
    if product_id:
        context['selected_product'] = get_object_or_404(Product, id=product_id)
    
    return render(request, 'ecommerce/category_details.html', context)
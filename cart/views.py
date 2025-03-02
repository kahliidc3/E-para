from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from products.models import Product
from .models import Cart, CartItem

@login_required(login_url='account_login')
def cart_detail(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    return render(request, 'cart/cart_detail.html', {'cart': cart})

@login_required(login_url='account_login')
def cart_add(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    
    if request.method == 'POST':
        quantity = int(request.POST.get('quantity', 1))
        if quantity > product.stock:
            messages.error(request, 'Not enough stock available.')
            return redirect('products:product_detail', slug=product.slug)
            
        cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
        if not created:
            cart_item.quantity += quantity
        else:
            cart_item.quantity = quantity
        cart_item.save()
        
        messages.success(request, 'Product added to cart.')
        return redirect('cart:cart_detail')
    
    return redirect('products:product_detail', slug=product.slug)

@login_required(login_url='account_login')
def cart_remove(request, product_id):
    cart = Cart.objects.get(user=request.user)
    product = get_object_or_404(Product, id=product_id)
    CartItem.objects.filter(cart=cart, product=product).delete()
    messages.success(request, 'Product removed from cart.')
    return redirect('cart:cart_detail')

@login_required(login_url='account_login')
def cart_update(request, product_id):
    cart = Cart.objects.get(user=request.user)
    product = get_object_or_404(Product, id=product_id)
    
    if request.method == 'POST':
        quantity = int(request.POST.get('quantity', 1))
        if quantity > product.stock:
            messages.error(request, 'Not enough stock available.')
        else:
            cart_item = get_object_or_404(CartItem, cart=cart, product=product)
            if quantity > 0:
                cart_item.quantity = quantity
                cart_item.save()
            else:
                cart_item.delete()
            messages.success(request, 'Cart updated.')
    
    return redirect('cart:cart_detail')

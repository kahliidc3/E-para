from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Order, OrderItem, Prescription
from cart.models import Cart
from accounts.models import Address

@login_required
def order_create(request):
    cart = Cart.objects.get(user=request.user)
    if not cart.items.exists():
        messages.error(request, 'Your cart is empty.')
        return redirect('cart:cart_detail')
    
    # Check if any product requires prescription
    requires_prescription = any(item.product.requires_prescription for item in cart.items.all())
    
    if request.method == 'POST':
        address_id = request.POST.get('address')
        payment_method = request.POST.get('payment_method')
        
        if not address_id:
            messages.error(request, 'Please select a delivery address.')
            return redirect('orders:order_create')
        
        address = get_object_or_404(Address, id=address_id, user=request.user)
        
        # Create order
        order = Order.objects.create(
            user=request.user,
            address=address,
            payment_method=payment_method
        )
        
        # Create order items
        for cart_item in cart.items.all():
            order_item = OrderItem.objects.create(
                order=order,
                product=cart_item.product,
                price=cart_item.product.price,
                quantity=cart_item.quantity
            )
            
            if cart_item.product.requires_prescription:
                Prescription.objects.create(order_item=order_item)
        
        # Clear the cart
        cart.items.all().delete()
        
        messages.success(request, 'Order placed successfully.')
        if requires_prescription:
            messages.info(request, 'Please upload prescriptions for required medications.')
        
        return redirect('orders:order_detail', order_id=order.id)
    
    addresses = Address.objects.filter(user=request.user)
    return render(request, 'orders/order_create.html', {
        'cart': cart,
        'addresses': addresses,
        'requires_prescription': requires_prescription
    })

@login_required
def order_list(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, 'orders/order_list.html', {'orders': orders})

@login_required
def order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    return render(request, 'orders/order_detail.html', {'order': order})

@login_required
def upload_prescription(request, order_item_id):
    order_item = get_object_or_404(OrderItem, id=order_item_id, order__user=request.user)
    
    if request.method == 'POST':
        prescription_image = request.FILES.get('prescription')
        if prescription_image:
            prescription = order_item.prescription
            prescription.image = prescription_image
            prescription.save()
            messages.success(request, 'Prescription uploaded successfully.')
        else:
            messages.error(request, 'Please select a prescription image to upload.')
    
    return redirect('orders:order_detail', order_id=order_item.order.id)

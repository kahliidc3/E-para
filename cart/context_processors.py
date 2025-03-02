from .models import Cart

def cart(request):
    if request.user.is_authenticated:
        cart_obj, created = Cart.objects.get_or_create(user=request.user)
        cart_count = sum(item.quantity for item in cart_obj.items.all())
        return {
            'cart': cart_obj,
            'cart_count': cart_count
        }
    return {
        'cart': None,
        'cart_count': 0
    }

from .models import Cart, CartItem
from .views import get_or_create_cart # Re-use the logic to get the cart

def cart_context(request):
    """
    Makes the cart and its item count available in all templates.
    """
    cart = get_or_create_cart(request)
    cart_items_count = cart.get_total_items() if cart else 0
    
    return {
        'current_cart': cart,
        'cart_items_count': cart_items_count
    }

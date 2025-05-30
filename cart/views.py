from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse, HttpResponseBadRequest
from django.views.decorators.http import require_POST
from shop.models import Product
from .models import Cart, CartItem
from django.contrib import messages

def get_or_create_cart(request):
    """
    Retrieves the current user's cart or creates a new one.
    If the user is authenticated, it uses their user ID.
    Otherwise, it uses the session key.
    """
    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user)
    else:
        session_key = request.session.session_key
        if not session_key:
            request.session.create()
            session_key = request.session.session_key
        cart, created = Cart.objects.get_or_create(session_key=session_key)
        # If an old cart existed for a logged-out user who now has a session key,
        # and that cart was associated with a user, we should probably create a new one
        # or handle merging. For simplicity, we ensure the cart is not user-associated if no user.
        if cart.user:
            cart = Cart.objects.create(session_key=session_key)

    return cart

def view_cart(request):
    """
    Displays the items in the shopping cart.
    """
    cart = get_or_create_cart(request)
    context = {
        'cart': cart,
        'cart_items': cart.items.all().order_by('added_at')
    }
    return render(request, 'view_cart.html', context)

@require_POST
def add_to_cart(request, product_pk):
    """
    Adds a product to the shopping cart or updates its quantity if it already exists.
    The quantity is taken from the 'quantity' POST parameter.
    """
    cart = get_or_create_cart(request)
    product = get_object_or_404(Product, pk=product_pk)
    
    quantity = request.POST.get('quantity', 1)
    try:
        quantity = int(quantity)
        if quantity < 1:
            quantity = 1
    except ValueError:
        quantity = 1

    cart_item, created = CartItem.objects.get_or_create(
        cart=cart,
        product=product,
        defaults={'quantity': quantity}
    )

    if not created:
        cart_item.quantity += quantity
        cart_item.save()
        messages.success(request, f"تعداد '{product.name}' در سبد خرید شما به‌روزرسانی شد.")
    else:
        messages.success(request, f"'{product.name}' با موفقیت به سبد خرید شما اضافه شد.")

    return redirect(request.POST.get('next', 'cart:view_cart'))


@require_POST
def remove_from_cart(request, item_pk):
    """
    Removes an item from the shopping cart.
    """
    cart_item = get_object_or_404(CartItem, pk=item_pk)
    
    # Ensure the item belongs to the current user's cart
    current_cart = get_or_create_cart(request)
    if cart_item.cart == current_cart:
        product_name = cart_item.product.name
        cart_item.delete()
        messages.success(request, f"'{product_name}' از سبد خرید شما حذف شد.")
    else:
        messages.error(request, "شما اجازه حذف این آیتم را ندارید.")
        
    return redirect('cart:view_cart')

@require_POST
def update_cart(request):
    """
    Updates the quantity of an item in the shopping cart.
    Expects 'item_pk' and 'quantity' in POST data.
    """
    item_pk = request.POST.get('item_pk')
    quantity_str = request.POST.get('quantity')

    if not item_pk or not quantity_str:
        messages.error(request, "اطلاعات ناقص برای به‌روزرسانی سبد خرید.")
        return redirect('cart:view_cart')

    try:
        quantity = int(quantity_str)
    except ValueError:
        messages.error(request, "مقدار تعداد نامعتبر است.")
        return redirect('cart:view_cart')

    cart_item = get_object_or_404(CartItem, pk=item_pk)
    current_cart = get_or_create_cart(request)

    if cart_item.cart != current_cart:
        messages.error(request, "شما اجازه به‌روزرسانی این آیتم را ندارید.")
        return redirect('cart:view_cart')

    if quantity > 0:
        cart_item.quantity = quantity
        cart_item.save()
        messages.success(request, f"تعداد '{cart_item.product.name}' به‌روزرسانی شد.")
    elif quantity == 0:
        product_name = cart_item.product.name
        cart_item.delete()
        messages.success(request, f"'{product_name}' از سبد خرید شما حذف شد.")
    else:
        messages.error(request, "تعداد نمی‌تواند منفی باشد.")

    return redirect('cart:view_cart')


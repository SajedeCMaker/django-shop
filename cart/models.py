from django.db import models
from django.contrib.auth.models import User
from shop.models import Product

class Cart(models.Model):
    """
    Model to represent a shopping cart.
    Each user can have one active cart.
    If the user is not authenticated, the cart can be associated with a session.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    session_key = models.CharField(max_length=40, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        if self.user:
            return f"Cart for {self.user.username}"
        return f"Cart for session {self.session_key}"

    def get_total_price(self):
        """
        Calculate the total price of all items in the cart.
        """
        return sum(item.get_total_price() for item in self.items.all())

    def get_total_items(self):
        """
        Calculate the total number of items in the cart.
        """
        return sum(item.quantity for item in self.items.all())

class CartItem(models.Model):
    """
    Model to represent an item within a shopping cart.
    """
    cart = models.ForeignKey(Cart, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.quantity} x {self.product.name} in cart {self.cart.id}"

    def get_total_price(self):
        """
        Calculate the total price for this cart item (product price * quantity).
        """
        if self.product.is_sale:
            return self.product.sale_price * self.quantity
        return self.product.price * self.quantity


from django.urls import path
from . import views

# It's good practice to add an app_name for namespacing if you have many apps
app_name = 'cart'

urlpatterns = [
    path('', views.view_cart, name='view_cart'),
    path('add/<int:product_pk>/', views.add_to_cart, name='add_to_cart'),
    path('remove/<int:item_pk>/', views.remove_from_cart, name='remove_from_cart'),
    path('update/', views.update_cart, name='update_cart'), # Changed from 'cart/update/' to just 'update/'
]
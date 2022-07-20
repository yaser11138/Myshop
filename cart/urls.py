from django.urls import path
from cart import views

app_name = "cart"

urlpatterns = [
    path("<int:product_id>/add/", views.add_cart, name="cart-add"),
    path("<int:product_id>/delete/", views.delete_cart, name="cart-delete"),
    path("detail/", views.cart_detail, name="cart-detail"),
    path("clear/", views.clear_cart, name="cart-clear"),
]
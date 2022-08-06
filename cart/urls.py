from django.urls import path
from cart import views

app_name = "cart"

urlpatterns = [
    path("<int:product_id>/add/", views.add_cart, name="product-add"),
    path("<int:product_id>/delete/", views.delete_cart, name="product-delete"),
    path("detail/", views.cart_detail, name="cart-detail"),
    path("clear/", views.clear_cart, name="cart-clear"),
]
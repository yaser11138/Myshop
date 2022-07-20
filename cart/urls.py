from django.urls import path
from cart import views

app_name= "cart"

urlpatterns = [
    path("<int:product_id>/add/", views.add_cart, name="add-cart"),
    path("<int:product_id>/delete/", views.delete_cart, name="delete-cart"),
    path("detail/", views.cart_detail, name="cart-detail")
]
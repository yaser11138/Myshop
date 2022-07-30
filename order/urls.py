from django.urls import path
from . import views

app_name = "order"

urlpatterns = [
    path("checkout/", views.checkout, name="checkout"),
    path("order/<int:order_id>/invoice/", views.invoice_creator, name="order-invoice")
]


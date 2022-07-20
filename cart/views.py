from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.views.decorators.http import require_POST
from django.conf import settings
from .cart import Cart
from .forms import CartForm
from shop.models import Product


@require_POST
def add_cart(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartForm(request.POST)
    if form.is_valid():
        override = form.cleaned_data["override"]
        qunatity = form.cleaned_data["quantity"]
        cart.add(product, quantity=qunatity, override_quantity=override)
    return redirect("cart:cart-detail")


@require_POST
def delete_cart(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.delete(product)
    print(request.session.get(settings.SESSION_CART_ID))
    return redirect("cart:cart-detail")


def clear_cart(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart:cart-detail")


def cart_detail(request):
    cart = Cart(request)

    return render(request, "cart/cart-detail.html", context={"cart": cart})
from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.views.decorators.http import require_POST
from django.utils.translation import gettext as _
from .cart import Cart
from .forms import CartUpdateForm
from shop.models import Product
from coupon.forms import CouponAddForm


@require_POST
def add_cart(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartUpdateForm(request.POST)
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
    return redirect("cart:cart-detail")


def clear_cart(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart:cart-detail")


def cart_detail(request):
    cart = Cart(request)
    cart_form = CartUpdateForm()
    coupon_form = CouponAddForm()
    return render(request, "cart/cart-detail.html", context={"cart": cart, "cart_form": cart_form,
                                                             "coupon_form": coupon_form})

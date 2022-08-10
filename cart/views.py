from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from .cart import Cart
from .forms import CartUpdateForm
from shop.models import Product
from coupon.forms import CouponAddForm
from shop.recommends import Recommender


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
    recommender = Recommender()
    products = [item["product"] for item in cart]
    recommends = recommender.suggest_products(products, max_result=3)   
    cart_form = CartUpdateForm()
    coupon_form = CouponAddForm()
    context = {
        "cart": cart,
        "cart_form": cart_form,
        "coupon_form": coupon_form,
        "recommends": recommends,
        }
    return render(request, "cart/cart-detail.html", context=context )

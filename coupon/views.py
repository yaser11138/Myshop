from django.shortcuts import redirect
from django.views.decorators.http import require_POST
from django.contrib import messages
from .forms import CouponAddForm


@require_POST
def coupon_validetor(request):
    coupon_form = CouponAddForm(request.POST)
    if coupon_form.is_valid():
        coupon = coupon_form.cleaned_data["code"]
        request.session["coupon-id"] = coupon.id
        return redirect("cart:cart-detail")
    else:

        messages.add_message(request, level=messages.ERROR, message=coupon_form.errors["code"])
        return redirect("cart:cart-detail")



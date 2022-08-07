from django.shortcuts import render, get_object_or_404, redirect
from order.models import Order
from .ziabal import Zibal
from cart.cart import Cart
from .tasks import invoice_sender


def request(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    zibal = Zibal()
    response = zibal.request(order.total_price, order_id,)
    track_id = response["trackId"]
    return redirect(f'https://gateway.zibal.ir/start/{track_id}')


def verify(request):
    track_id = request.GET.get("trackId")
    cart = Cart(request)
    zibal = Zibal()
    payment_detail = zibal.verify(track_id)
    if payment_detail["result"] == 100:
        order = get_object_or_404(Order, id=payment_detail["orderId"])
        order.paid = True
        order.save()
        invoice_sender.delay(order.id)
        cart.clear()
        cart.clear_coupon()
    return render(request, "zibal/payment-verify.html", {"payment_detail": payment_detail})

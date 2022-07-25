from django.shortcuts import render, HttpResponse
from cart.cart import Cart
from .forms import AddOrderform
from .models import OrderItem
from .tasks import create_email


def checkout(request):
    cart = Cart(request)
    if request.method == "POST":
        form = AddOrderform(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order, product=item["product"], quantity=item["quantity"],
                                         price=item["price"])
            cart.clear()
            create_email.delay(order.id)
            return HttpResponse(f"your order is created {order.id}")
        return render(request, "order/checkout.html", {"form": form})
    else:
        form = AddOrderform()
        return render(request, "order/checkout.html", {"form": form})

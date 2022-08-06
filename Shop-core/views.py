from django.shortcuts import render
from shop.models import Product


def homepage(request):
    new_products = Product.objects.order_by("-id")[0:5]
    return render(request, "index.html", {"new_products": new_products})


def about(request):
    return render(request, "about.html")
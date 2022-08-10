from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from cart.forms import CartUpdateForm
from .recommends import Recommender


def products_list(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    context = {
        "products": products,
        "categories": categories,
    }
    return render(request, "shop/product-list.html", context=context)


def product_list_by_category(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    categories = Category.objects.all()
    products = products.filter(category=category)
    context = {
        "products": products,
        "categories": categories,
        "category": category,
    }
    return render(request, "shop/product-list.html", context=context)


def product_detail(request, id, product_slug):
    product = get_object_or_404(Product, id=id, slug=product_slug)
    form = CartUpdateForm()
    recommander = Recommender()
    recommends = recommander.suggest_products([product], max_result=3)
    context = {
        "product": product,
        "form": form,
        "recommends": recommends,
    }
    return render(request, "shop/product-detail.html", context=context)

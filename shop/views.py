from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from cart.forms import CartUpdateForm


def products_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.all()
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
        context = {
            "products": products,
            "categories": categories,
            "category": category,
        }
    else:
        context = {
            "products": products,
            "categories": categories,
        }
    return render(request, "shop/product-list.html", context=context)


def product_detail(request, id, product_slug):
    product = get_object_or_404(Product, id=id, slug=product_slug)
    form = CartUpdateForm()
    context = {
        "product": product,
        "form": form
    }
    return render(request, "shop/product-detail.html", context=context)



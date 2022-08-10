from django.urls import path, include
from shop import views

app_name = "shop"

urlpatterns = [
    path("product-list", views.products_list, name="product-list"),
    path("<slug:category_slug>/list", views.product_list_by_category, name="product-list-by-category"),
    path("<int:id>/<slug:product_slug>/detail", views.product_detail, name="product-detail"),

]
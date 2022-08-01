from django.urls import path
from . import views

app_name = "coupon"

urlpatterns = [
    path("verify/", views.coupon_validetor, name="verify")
]

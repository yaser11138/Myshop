from django.urls import path
from . import views

app_name = "zibal"

urlpatterns = [
    path("request/<int:order_id>/", views.request, name="request"),
    path("verify/", views.verify, name="verify")
]
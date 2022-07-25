from django import forms
from .models import Order


class AddOrderform(forms.ModelForm):
    class Meta:
        model = Order
        fields = ["first_name", "last_name", "email","state", "city", "address", "postal_code"]

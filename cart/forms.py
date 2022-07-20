from django import forms


PRODUCT_QUANTITY_CHOICES = ((i, i) for i in range(1, 21))


class CartForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES, coerce=str)
    override = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)


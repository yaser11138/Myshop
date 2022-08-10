from django import forms


class CartUpdateForm(forms.Form):
    quantity = forms.IntegerField("Quantity")
    override = forms.BooleanField(required=False,initial=False, widget=forms.HiddenInput)

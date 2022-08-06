from django import forms
from django.utils.translation import gettext as _


class CartUpdateForm(forms.Form):
    quantity = forms.IntegerField(label=_("Quantity"))
    override = forms.BooleanField(required=False,initial=False, widget=forms.HiddenInput)

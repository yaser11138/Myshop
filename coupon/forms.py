from django import forms
from django.core.exceptions import ObjectDoesNotExist
from django.utils import timezone
from .models import Coupon


class CouponAddForm(forms.Form):
    code = forms.CharField()

    def clean_code(self):
        now = timezone.now()
        code = self.cleaned_data["code"]
        try:
            coupun = Coupon.objects.get(code=code)
            if coupun.is_valid(now) and coupun.activate:
                return coupun
            else:
                raise forms.ValidationError("the coupon is not valid")
        except ObjectDoesNotExist:
            raise forms.ValidationError("the coupon is not found")

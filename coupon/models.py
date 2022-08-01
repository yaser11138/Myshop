from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Coupon(models.Model):
    code = models.CharField(unique=True, max_length=5)
    date_from = models.DateTimeField()
    date_to = models.DateTimeField()
    discount = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    activate = models.BooleanField()

    def __str__(self):
        return self.code

    def is_valid(self, time):
        if self.date_from < time < self.date_to:
            return True
        else:
            return False

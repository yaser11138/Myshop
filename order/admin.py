from django.contrib import admin
from .models import Order, OrderItem


class OredrItemInline(admin.StackedInline):
    model = OrderItem


@admin.register(Order)
class OrderAmin(admin.ModelAdmin):
    list_display = ["id", "first_name", "last_name", "city", "state", "address", "paid", "created"]
    list_filter = ("first_name", "last_name", "created", "city", "state")
    inlines = [OredrItemInline]

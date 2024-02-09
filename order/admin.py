import csv
import datetime
from django.shortcuts import reverse
from django.contrib import admin
from django.http import HttpResponse
from django.utils.safestring import mark_safe
from .models import Order, OrderItem

import os
import platform

if platform.system() == 'Windows':
    os.add_dll_directory(r"C:\Program Files\GTK3-Runtime Win64\bin")

class OredrItemInline(admin.StackedInline):
    model = OrderItem


def csv_creator(filename):
    csv_file = HttpResponse(
        content_type="text/csv",
        headers={'Content-Disposition': f'attachment; filename="{filename}.csv"'})
    return csv_file


def csv_file_writer(csv_file, fields, objects):
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow([field.verbose_name for field in fields])
    for obj in objects:
        data_row = []
        for field in fields:
            value = getattr(obj, field.name)
            if isinstance(value, datetime.datetime):
                value = value.strftime("%Y-%m-%D")
            data_row.append(value)
        csv_writer.writerow(data_row)
    return csv_file


def export_csv(self, request, queryset):
    order_meta_options = self.model._meta
    fields = [field for field in order_meta_options.get_fields() if not field.many_to_many and not field.one_to_many]
    csv_file = csv_creator("My Shop - Orders")
    orders_csv = csv_file_writer(csv_file, fields, queryset)
    return orders_csv


def pdf_view(obj):
    url = reverse("order:order-invoice", args=[obj.id])
    return mark_safe(f"<a href={url}>PDF</a>")


@admin.register(Order)
class OrderAmin(admin.ModelAdmin):
    list_display = ["id", "first_name", "last_name", "city", "state", "address", "paid", "created", pdf_view]
    list_filter = ("first_name", "last_name", "created", "city", "state")
    inlines = [OredrItemInline]
    actions = [export_csv]


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    pass


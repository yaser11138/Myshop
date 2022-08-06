from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from .models import Product, Category


class AvailableFilter(admin.SimpleListFilter):
    # Human-readable title which will be displayed in the
    # right admin sidebar just above the filter options.
    title = _('Available')

    # Parameter for the filter that will be used in the URL query.
    parameter_name = 'Available'

    def lookups(self, request, model_admin):

        return (
            ('True', _('Available Product')),
            ('False', _('unavailable Product')),
        )

    def queryset(self, request, queryset):
        # Compare the requested value (either 'True' or 'False')
        # to decide how to filter the queryset.
        if self.value() == 'True':
            return queryset.filter(
                amount__gt=0
            )
        if self.value() == 'False':
            return queryset.filter(
                amount=0
            )


@admin.register(Category)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["name", "slug"]
    prepopulated_fields = {"slug": ["name"]}


@admin.register(Product)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["id","name", "slug", "price", "amount", "updated", "available"]
    prepopulated_fields = {"slug": ["name"]}
    list_filter = ["name", "price", AvailableFilter]
    search_fields = ["name", "price"]

    def available(self, obj):
        return obj.available

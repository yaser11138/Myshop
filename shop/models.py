from django.db import models
from django.urls import reverse
from django.utils.translation import gettext as _


class Category(models.Model):
    name = models.CharField(_("name"), max_length=200, db_index=True)
    slug = models.SlugField(_("slug"), max_length=200, db_index=True)

    class Meta:
        ordering = ("name",)
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")

    def __str__(self):
        return self.name


def user_directory_path(instance, filename):
    return f'product_{instance.name}/{filename}'


class Product(models.Model):
    category = models.ForeignKey(Category, related_name="products", on_delete=models.CASCADE,
                                 verbose_name=_("Category"))
    name = models.CharField(_("name"), max_length=200, db_index=True)
    slug = models.SlugField(_("slug"), max_length=200, db_index=True)
    description = models.TextField(_("description"), blank=True)
    price = models.PositiveIntegerField(_("price"))
    image = models.ImageField(_("image"), blank=True, upload_to=user_directory_path)
    amount = models.PositiveIntegerField(_("amount"))
    created = models.DateField(_("created"), auto_now_add=True)
    updated = models.DateField(_("updated"), auto_now=True)

    @property
    def available(self):
        return self.amount > 0

    class Meta:
        ordering = ("-updated",)
        index_together = (("id", "slug"),)
        verbose_name = _("product")
        verbose_name_plural = _("products")

    def get_absloute_url(self):
        return reverse("shop:product-detail", kwargs={"id": self.id, "product_slug": self.slug})

    def __str__(self):
        return self.name

from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)

    class Meta:
        ordering = ("name",)
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT / user_<id>/<filename>
    return f'product_{instance.name}/{filename}'


# noinspection PyUnresolvedReferences
class Product(models.Model):
    category = models.ForeignKey(Category, related_name="products", on_delete=models.CASCADE)
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    description = models.TextField(blank=True)
    price = models.PositiveIntegerField()
    image = models.ImageField(blank=True, upload_to=user_directory_path)
    amount = models.PositiveIntegerField()
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    @property
    def available(self):
        return self.amount > 0

    class Meta:
        ordering = ("updated",)
        index_together = (("id", "slug"),)

    def get_absloute_url(self):
        return reverse("product-detail", kwargs={"id": self.id, "product_slug": self.slug})

    def __str__(self):
        return self.name

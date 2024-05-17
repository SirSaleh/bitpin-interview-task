from django.utils.translation import gettext_lazy as _
from django.utils.timezone import now
from django.contrib.auth.models import User
from django.db import models


class Product(models.Model):
    title = models.CharField(verbose_name=_("Title"), max_length=128)

    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("Products")


class ProductRating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_("User"))
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name=_("Product"))
    rating = models.SmallIntegerField(verbose_name=_("Rating"))
    timestamp = models.DateTimeField(default=now)

    class Meta:
        verbose_name = _("Product Rating")
        verbose_name_plural = _("Product Ratings")

        unique_together = ("user", "product")


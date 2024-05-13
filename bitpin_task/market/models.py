from django.utils.translation import gettext_lazy as _
from django.db import models


class Product(models.Model):
    title = models.CharField(verbose_name=_("Title"), max_length=128)

    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("Products")

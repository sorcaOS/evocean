from django.db import models

from marketplace.models.product import Product


class TemplateFormat(models.Model):
    name = models.CharField(max_length=255)
    theme = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="template_formats"
    )

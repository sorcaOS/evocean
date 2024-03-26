from django.db import models

from marketplace.models.uploaded_image import UploadedImage


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    price_unit = models.CharField(max_length=10, default="sol")
    overview = models.TextField(null=True, blank=True)
    highlight = models.TextField(null=True, blank=True)
    author = models.ForeignKey(
        "auth.User", on_delete=models.CASCADE, related_name="products_authored"
    )

    def get_upload_path(self, filename):
        return f"themes/{self.name}/{filename}"

    thumbnail_image = models.ForeignKey(
        UploadedImage,
        on_delete=models.CASCADE,
        related_name="product_thumbnail_image",
        null=True,
        blank=True,
    )
    preview_images = models.ManyToManyField(
        UploadedImage, related_name="theme_preview_images"
    )
    theme_file = models.FileField(upload_to=get_upload_path)

    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class CategoryChoices(models.TextChoices):
        UI_KIT = "UI_KIT", "UI Kit"
        TEMPLATE = "TEMPLATE", "Template"
        FRAMER = "FRAMER", "Framer"
        WEBFLOW = "WEBFLOW", "Webflow"
        BADGE = "BADGE", "Badge"
        CODED_TEMPLATE = "CODED_TEMPLATE", "Coded Templates"

    category = models.CharField(
        max_length=50, choices=CategoryChoices.choices, default=CategoryChoices.UI_KIT
    )

    is_featured = models.BooleanField(default=False)
    owner = models.ForeignKey(
        "auth.User", on_delete=models.CASCADE, related_name="products"
    )
    section_count = models.IntegerField(default=0)
    is_day_and_night_mode = models.BooleanField(default=False)
    remaining_products = models.IntegerField(default=0)

    def __str__(self):
        return self.name

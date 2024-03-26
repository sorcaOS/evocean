import glob
import os

import django


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "evocean_django.settings")
django.setup()

from marketplace.models.product import Product


product_query = Product.objects.filter(highlight__isnull=True)

product_query.update(
    highlight="""Auto Dark Theme available
Fully repsponsive
Detailed inveractive component
3 homepage layout
5 primary page layouts
4 content pages layouts
32+ different sections"""
)

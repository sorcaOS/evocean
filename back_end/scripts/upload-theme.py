import glob
import os
from io import BytesIO

import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "evocean_django.settings")
django.setup()
from django.core.files.base import ContentFile
from django.db.models import ImageField

from marketplace.models.uploaded_image import UploadedImage

from django.db import IntegrityError
from rest_framework.authtoken.admin import User

from marketplace.models.product import Product

import pandas as pd

theme_folder = glob.glob("data/uploaded_theme/*")


def set_image_input_by_path(image_field: ImageField, path: str, file_name: str = None):
    """
    Set the image input by the url
    """

    _io = open(path, "rb")
    content_file = ContentFile(BytesIO(_io.read()).read())
    if not file_name:
        file_name = "/".join(path.split("/")[-3:])
    image_field.save(file_name, content_file, save=True)


for theme_path in theme_folder:
    content_name = glob.glob(theme_path + "/*.xlsx")[0]
    df = pd.read_excel(content_name)
    print(df)
    # Name	Short Description	Price Sol	Oeverview	Highlight	Format	Category	Owner	Section Count	Is Day And Night Mode
    name = df["Name"][0]
    is_exists = Product.objects.filter(name=name).exists()
    if is_exists:
        continue
    short_description = df["Short Description"][0]
    price = df["Price Sol"][0]
    overview = df["Overview"][0]
    highlight = df["Highlight"][0]
    formats = df["Format"][0].split("\n")
    category = df["Category"][0]
    owner_username = df["Owner"][0].replace(" ", "")
    section_count = df["Section Count"][0]
    is_day_and_night_mode = bool(df["Is Day And Night Mode"][0])
    # delete all uploaded images
    # UploadedImage.objects.all().delete()
    # Create new user or get if exists
    try:
        owner, created = User.objects.get_or_create(username=owner_username)
    except IntegrityError:
        owner = User.objects.get(username=owner_username)

    theme, _ = Product.objects.get_or_create(
        name=name,
        defaults={
            "description": short_description,
            "price": price,
            "price_unit": "sol",
            "category": category,
            "owner": owner,
            "section_count": section_count,
            "is_day_and_night_mode": is_day_and_night_mode,
        },
    )
    theme.template_formats.all().delete()

    for format in formats:
        theme.template_formats.get_or_create(name=format)
    theme.save()

    preview_images = glob.glob(theme_path + "/preview_images/*")

    for path in preview_images:
        file_name = "/".join(path.split("/")[-3:])
        uploaded_image = UploadedImage.objects.get_or_create(file_name=file_name)[0]
        theme.preview_images.add(uploaded_image)
        set_image_input_by_path(uploaded_image.image, path)
        uploaded_image.save()
    thumbnail_image = glob.glob(theme_path + "/Preview_images/1.*")[0]
    file_name = "/".join(thumbnail_image.split("/")[-3:])
    uploaded_image = UploadedImage.objects.get_or_create(file_name=file_name)[0]
    theme.thumbnail_image = uploaded_image
    set_image_input_by_path(uploaded_image.image, thumbnail_image)
    uploaded_image.save()
    theme.save()
    print(theme)

from django.db import models
from shortuuid import ShortUUID


class UploadedImage(models.Model):

    def get_upload_path(self, filename):
        short_uid = ShortUUID()
        return f"images/{filename}"

    image = models.ImageField(upload_to=get_upload_path)
    file_name = models.CharField(max_length=512, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.image.url

from django.db import models
from django.utils.safestring import mark_safe


class News(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    body_text = models.TextField()
    image = models.ImageField()
    date = models.DateField()
    URL = models.URLField()

    def admin_photo(self):
        return mark_safe(f'<img src="{self.image.url}" style="max-height: 100px;"/>')

    admin_photo.short_descrition = 'Image'
    admin_photo.allow_tags = True

    def __str__(self) -> str:
        return self.title


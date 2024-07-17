from django.db import models
from django.utils.safestring import mark_safe


class About_Us(models.Model):
    title = models.CharField(max_length=255)
    body_text = models.TextField()

    def __str__(self) -> str:
        return self.title


class Our_Certificate(models.Model):
    certificate = models.ImageField()

    def admin_photo(self):
        return mark_safe(f'<img src="{self.certificate.url}" style="max-height: 100px;"/>')
    admin_photo.short_descrition = 'Certificate'
    admin_photo.allow_tags = True


class Company_License(models.Model):
    title = models.CharField(max_length=255)
    about = models.TextField()
    license = models.ImageField()

    def admin_photo(self):
        return mark_safe(f'<img src="{self.license.url}" style="max-height: 100px;"/>')
    admin_photo.short_descrition = 'License'
    admin_photo.allow_tags = True

    def __str__(self) -> str:
        return self.title
from django.db import models
from django.utils.safestring import mark_safe


# Products and services that are on the home page


class Home(models.Model):
    title = models.CharField(max_length=255)
    about = models.TextField()
    img = models.ImageField()  # Image of product/service

    def admin_photo(self):
        return mark_safe(f'<img src="{self.img.url}" style="max-height: 100px;"/>')

    admin_photo.short_descrition = 'Image'
    admin_photo.allow_tags = True

    def __str__(self) -> str:
        return self.title


# Certificates at home page


class Certificate(models.Model):
    title = models.CharField(max_length=255)
    about = models.TextField()
    img = models.ImageField()  # Image of certificate

    def admin_photo(self):
        return mark_safe(f'<img src="{self.img.url}" style="max-height: 100px;"/>')

    admin_photo.short_descrition = 'Image'
    admin_photo.allow_tags = True

    def __str__(self) -> str:
        return self.title


# Fields of Activities at home page(for example, 12+ Qualified specialists)


class FieldOfActivity(models.Model):
    title = models.CharField(max_length=255)
    num = models.CharField(max_length=5)  # 12+ / 2+ / 3+ / 4,5b / 1,2m / 6,7k+

    def __str__(self) -> str:
        return self.title


class Partner(models.Model):
    name = models.CharField(max_length=255)  # Name of partner
    url = models.URLField()  # URL to partner

    def __str__(self) -> str:
        return self.name


class Contact(models.Model):
    title = models.CharField(max_length=255)  # Social network/phone num/email
    icon = models.ImageField()

    def admin_photo(self):
        return mark_safe(f'<img src="{self.icon.url}" style="max-height: 100px;"/>')

    admin_photo.short_descrition = 'Icon'
    admin_photo.allow_tags = True

    def __str__(self) -> str:
        return self.title

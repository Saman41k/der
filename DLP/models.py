from django.db import models
from django.utils.safestring import mark_safe


class DatagazeDLP(models.Model):
    title = models.CharField(max_length=255)
    about = models.TextField()

    def __str__(self) -> str:
        return self.title

# PartsOfDatagazeDLP


class Parts(models.Model):
    title = models.CharField(max_length=255)
    about = models.TextField()
    icon = models.ImageField()

    def admin_photo(self):
        return mark_safe(f'<img src="{self.icon.url}" style="max-height: 100px;"/>')
    admin_photo.short_descrition = 'Icon'
    admin_photo.allow_tags = True

    def __str__(self) -> str:
        return self.title

# Features of Datagaze DLP


class Features(models.Model):
    title = models.CharField(max_length=255)
    icon = models.ImageField()

    def admin_photo(self):
        return mark_safe(f'<img src="{self.icon.url}" style="max-height: 100px;"/>')
    admin_photo.short_descrition = 'Icon'
    admin_photo.allow_tags = True

    def __str__(self) -> str:
        return self.title

# Information channels controlled by Datagaze DLP


class Channel(models.Model):
    title = models.CharField(max_length=255)
    icon = models.ImageField()

    def admin_photo(self):
        return mark_safe(f'<img src="{self.icon.url}" style="max-height: 100px;"/>')
    admin_photo.short_descrition = 'Icon'
    admin_photo.allow_tags = True

    def __str__(self) -> str:
        return self.title

# Working enviroment of Datagaze DLP


class Environment(models.Model):
    ENV_CHOICES = [('C', 'Client'), ('S', 'Server')]
    title = models.CharField(max_length=255)
    category = models.CharField(max_length=255, choices=ENV_CHOICES)
    icon = models.ImageField()

    def admin_photo(self):
        return mark_safe(f'<img src="{self.icon.url}" style="max-height: 100px;"/>')
    admin_photo.short_descrition = 'Icon'
    admin_photo.allow_tags = True

    def __str__(self) -> str:
        return self.title

# Installing and configuring Datagaze DLP


class I_and_C(models.Model):
    title = models.CharField(max_length=255)
    time = models.FloatField()  # time in hours
    image = models.ImageField()

    def admin_photo(self):
        return mark_safe(f'<img src="{self.image.url}" style="max-height: 100px;"/>')
    admin_photo.short_descrition = 'Image'
    admin_photo.allow_tags = True

    def __str__(self) -> str:
        return self.title


class Screenshot(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField()

    def admin_photo(self):
        return mark_safe(f'<img src="{self.image.url}" style="max-height: 100px;"/>')
    admin_photo.short_descrition = 'Image'
    admin_photo.allow_tags = True

    def __str__(self) -> str:
        return self.title


class Video(models.Model):
    title = models.CharField(max_length=255)
    video = models.URLField()

    def __str__(self) -> str:
        return self.title


class Order(models.Model):
    title = models.CharField(max_length=255)
    icon = models.ImageField()

    def admin_photo(self):
        return mark_safe(f'<img src="{self.icon.url}" style="max-height: 100px;"/>')
    admin_photo.short_descrition = 'Icon'
    admin_photo.allow_tags = True

    def __str__(self) -> str:
        return self.title

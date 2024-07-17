from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import About_Us, Company_License, Our_Certificate


@admin.register(About_Us)
class About_UsAdmin(TranslationAdmin):
    list_display = ('title', 'body_text')
    search_fields = ('title',)
    group_fieldsets = True

    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


@admin.register(Company_License)
class Company_LicenseAdmin(TranslationAdmin):
    list_display = ('title', 'about', 'admin_photo')
    search_fields = ('title',)
    group_fieldsets = True

    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


@admin.register(Our_Certificate)
class Our_CertificateAdmin(admin.ModelAdmin):
    list_display = ('admin_photo',)
    group_fieldsets = True
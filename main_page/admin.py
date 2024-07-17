from modeltranslation.admin import TranslationAdmin
from django.contrib import admin
from .models import Home, FieldOfActivity, Certificate, Partner, Contact


@admin.register(Home)
class HomeAdmin(TranslationAdmin):
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


@admin.register(FieldOfActivity)
class FieldOfActivityAdmin(TranslationAdmin):
    list_display = ('title', 'num')
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


@admin.register(Certificate)
class CertificateAdmin(TranslationAdmin):
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


@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = ('name', 'url')
    search_fields = ('title',)


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('title', 'admin_photo')
    search_fields = ('title',)

from modeltranslation.translator import register, TranslationOptions
from .models import About_Us, Company_License, Our_Certificate


@register(About_Us)
class About_UsTranslationOptions(TranslationOptions):
    fields = ('title', 'body_text')


@register(Company_License)
class Company_LicenseTranslationOptions(TranslationOptions):
    fields = ('title', 'about')

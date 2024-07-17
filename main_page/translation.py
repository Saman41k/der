from modeltranslation.translator import register, TranslationOptions
from .models import Home, Certificate, FieldOfActivity, Partner, Contact

@register(Home)
class HomeTranslationOptions(TranslationOptions):
    fields = ('title', 'about')
@register(Certificate)
class CertificateTranslationOptions(TranslationOptions):
    fields = ('title', 'about')
@register(FieldOfActivity)
class HomeTranslationOptions(TranslationOptions):
    fields = ('title',)
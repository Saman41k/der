# myapp/translation.py
from modeltranslation.translator import register, TranslationOptions
from .models import DatagazeDLP, Parts, Features, Channel, I_and_C, Screenshot, Video, Order


@register(DatagazeDLP)
class DatagazeDLPTranslationOptions(TranslationOptions):
    fields = ('title', 'about')


@register(Parts)
class PartsTranslation(TranslationOptions):
    fields = ('title', 'about')


@register(Features)
class FeaturesTranslation(TranslationOptions):
    fields = ('title',)


@register(Channel)
class ChannelTranslation(TranslationOptions):
    fields = ('title',)


@register(I_and_C)
class I_and_CTranslation(TranslationOptions):
    fields = ('title',)


@register(Screenshot)
class ScreenshotTranslation(TranslationOptions):
    fields = ('title',)


@register(Video)
class VideoTranslation(TranslationOptions):
    fields = ('title',)


@register(Order)
class OrderTranslation(TranslationOptions):
    fields = ('title',)

from django.urls import path, include
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()

router.register('dlp', DatagazeDLPViewSet)
router.register('parts', PartsViewSet)
router.register('features', FeaturesViewSet)
router.register('channels', ChannelViewSet)
router.register('env', EnvironmentViewSet)
router.register('i-c', I_and_CViewSet)
router.register('screenshots', ScreenshotViewSet)
router.register('videos', VideoViewSet)
router.register('orders', OrderViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

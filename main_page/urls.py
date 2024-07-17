from django.urls import path, include
from .views import HomeViewSet, CeritificateViewSet, PartnerViewSet, ContactViewSet, FieldOfActivityViewSet
from rest_framework import routers

router = routers.DefaultRouter()

router.register('home', HomeViewSet)
router.register('certificate', CeritificateViewSet)
router.register('partner', PartnerViewSet)
router.register('contact', ContactViewSet)
router.register('fieldsofactivity', FieldOfActivityViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
from django.urls import path, include
from rest_framework import routers
from .views import About_UsViewSet, Our_CertificateViewSet, Company_LicenseViewSet

router = routers.DefaultRouter()

router.register('about', About_UsViewSet)
router.register('our-certificate', Our_CertificateViewSet)
router.register('company-licesnse', Company_LicenseViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
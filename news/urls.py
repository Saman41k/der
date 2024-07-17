from django.urls import path, include
from .views import NewsViewSet
from rest_framework import routers

router = routers.DefaultRouter()

router.register('news', NewsViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
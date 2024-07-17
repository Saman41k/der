from rest_framework import viewsets, mixins
from .models import *
from .serializers import *


class DatagazeDLPViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = DatagazeDLP.objects.all()
    serializer_class = DatagazeDLPSerializer


class PartsViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Parts.objects.all()
    serializer_class = PartsSerializer


class FeaturesViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Features.objects.all()
    serializer_class = FeaturesSerializer


class ChannelViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Channel.objects.all()
    serializer_class = ChannelSerializer


class EnvironmentViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Environment.objects.all()
    serializer_class = EnvironmentSerializer


class I_and_CViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = I_and_C.objects.all()
    serializer_class = I_and_CSerializer


class ScreenshotViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Screenshot.objects.all()
    serializer_class = ScreenshotSerializer


class VideoViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer


class OrderViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

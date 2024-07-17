from rest_framework import serializers
from .models import *


class DatagazeDLPSerializer(serializers.ModelSerializer):
    class Meta:
        model = DatagazeDLP
        fields = ['id', 'title', 'about']


class PartsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parts
        fields = ['id', 'title', 'about', 'icon']


class FeaturesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Features
        fields = ['id', 'title', 'icon']


class ChannelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Channel
        fields = ['id', 'title', 'icon']


class EnvironmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Environment
        fields = ['id', 'title', 'category', 'icon']


class I_and_CSerializer(serializers.ModelSerializer):
    class Meta:
        model = I_and_C
        fields = ['id', 'title', 'time', 'image']


class ScreenshotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Screenshot
        fields = ['id', 'title', 'image']


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ['id', 'title', 'video']


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'title', 'icon']

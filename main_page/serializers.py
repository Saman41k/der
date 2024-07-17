from rest_framework import serializers
from .models import Home, Certificate, FieldOfActivity, Partner, Contact

class HomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Home
        fields = ('id', 'title', 'about', 'img')

class CertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificate
        fields = ('id', 'title', 'about', 'img')

class FieldOfActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = FieldOfActivity
        fields = ('id', 'title', 'num')

class PartnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partner
        fields = ('id', 'name', 'url')

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ('id', 'title', 'icon')
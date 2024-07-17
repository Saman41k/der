from rest_framework import serializers
from  .models import About_Us, Our_Certificate, Company_License

class About_UsSerializer(serializers.ModelSerializer):
    class Meta:
        model = About_Us
        fields = ('id', 'title', 'body_text')

class Our_CertificatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Our_Certificate
        fields = ('id', 'certificate')

class Company_LicensesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company_License
        fields = ('id', 'title', 'about', 'license')
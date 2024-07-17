from rest_framework import mixins, viewsets
from .serializers import HomeSerializer, CertificateSerializer, PartnerSerializer, ContactSerializer, FieldOfActivitySerializer
from .models import Home, Certificate, Partner, Contact, FieldOfActivity

class HomeViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Home.objects.all()
    serializer_class = HomeSerializer

class CeritificateViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer

class PartnerViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Partner.objects.all()
    serializer_class = PartnerSerializer

class ContactViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

class FieldOfActivityViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = FieldOfActivity.objects.all()
    serializer_class = FieldOfActivitySerializer
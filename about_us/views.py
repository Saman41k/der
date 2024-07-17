from rest_framework import mixins, viewsets
from .models import About_Us, Our_Certificate, Company_License
from .serializers import About_UsSerializer, Our_CertificatesSerializer, Company_LicensesSerializer


class About_UsViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = About_Us.objects.all()
    serializer_class = About_UsSerializer


class Our_CertificateViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Our_Certificate.objects.all()
    serializer_class = Our_CertificatesSerializer


class Company_LicenseViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Company_License.objects.all()
    serializer_class = Company_LicensesSerializer

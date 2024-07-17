from rest_framework import mixins, viewsets
from .models import News
from .serializers import NewsSerializer

class NewsViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.views.i18n import set_language

schema_view = get_schema_view(
    openapi.Info(
        title='Swagger Datagaze',
        default_version='v1',
        description='Swagger Datagaze API',
        terms_of_service='https://www.ourapp.com/policies/terms/',
        contact=openapi.Contact(email='contact@swaggerBlog.local'),
        license=openapi.License(name='Test License'),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('i18n/', set_language, name='set_language'),
    path('main/', include('main_page.urls')),
    path('dlp/', include('DLP.urls')),
    path('news/', include('news.urls')),
    path('about_us/', include('about_us.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

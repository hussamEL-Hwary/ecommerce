"""
URL configuration for ecommerce project.
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from oauth2_provider import urls as oauth2_urls
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework.authentication import SessionAuthentication


openapi_info = openapi.Info(
    title="Ecommerce API",
    default_version='v1',
    description="API Endpoints for AEcommerce",
    contact=openapi.Contact(name="InnovaDigits", email="info@innovadigits.com",
                            url="https://innovadigits.com/"),
    license=openapi.License(name="InnovaDigits", url="https://innovadigits.com/"),
)

api = [
    path('o/', include(oauth2_urls)),
    path('api/', include('users.urls')),
]


# swagger endpoint docs
schema_view = get_schema_view(openapi_info, url=settings.VIEW_SITE_URL,
                              patterns=api,
                              authentication_classes=[SessionAuthentication])

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/docs/swagger/', schema_view.with_ui('swagger', cache_timeout=0),
         name='schema-swagger'),
]+api

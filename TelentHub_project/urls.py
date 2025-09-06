from django.contrib import admin
from django.urls import path,include
from .views import api_root_view
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="TalentHub API",
      default_version='v1',
      description="API Documentations for TalentHub Project ",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="sujonahmed.22.03@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',api_root_view),
    path('api-auth/', include('rest_framework.urls')),
    path('api/v1/',include('api.urls'),name='api-root'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc')
    
]

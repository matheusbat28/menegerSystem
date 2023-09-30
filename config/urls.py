from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from countries.views import CountriesViewSet
from rest_framework import routers



schema_view = get_schema_view(
    openapi.Info(
        title="Snippets API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="", url=""),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.IsAuthenticated,),
)

router = routers.DefaultRouter()
router.register(r'countries', CountriesViewSet, basename='countries')

urlpatterns = [
    # django
    path('admin/', admin.site.urls),
    # swagger
    path('api/v1/swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('api/v1/redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    # rest framework
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # autentificacion
    path('api/v1/', include('djoser.urls')),
    path('api/v1/', include('djoser.urls.jwt')),
    # app
    path('api/v1/', include(router.urls)),
]


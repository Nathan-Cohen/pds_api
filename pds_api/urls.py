from django.contrib import admin
from django.urls import path, include
from rest_framework_swagger.views import get_swagger_view
from rest_framework import routers
from api.urls import router as api_router

router = routers.DefaultRouter()
router.registry.extend(api_router.registry)

schema_view = get_swagger_view(title='Base PDS API')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('schemaApi/', schema_view),
]

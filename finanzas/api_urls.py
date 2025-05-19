from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api_views import RegistroFinancieroViewSet

router = DefaultRouter()
router.register(r'registros', RegistroFinancieroViewSet, basename='registro')

urlpatterns = [
    path('', include(router.urls)),
]

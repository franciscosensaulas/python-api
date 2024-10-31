from django.urls import include, path
from rest_framework import routers

from api.views import CategoriaViewSet

router = routers.DefaultRouter()
router.register('categorias', CategoriaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

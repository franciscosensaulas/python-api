
from django.urls import include, path
from rest_framework import routers

from api.views import CategoriaViewSet, JogoViewSet


router = routers.DefaultRouter()
router.register('categorias', CategoriaViewSet)
router.register('jogos', JogoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

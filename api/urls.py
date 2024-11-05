
from django.urls import include, path
from rest_framework import routers

from api.views import CategoriaViewSet, ClienteCriarView, CustomTokenObtainPairView, JogoViewSet


router = routers.DefaultRouter()
router.register('categorias', CategoriaViewSet)
router.register('jogos', JogoViewSet)
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('', include(router.urls)),
    path('cliente/cadastro/', ClienteCriarView.as_view(), name='registro_cliente'),
    path('login/', CustomTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path('token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
]

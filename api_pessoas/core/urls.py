from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PessoaViewSet, EnderecoViewSet

router = DefaultRouter()
router.register(r'pessoas', PessoaViewSet)
router.register(r'enderecos', EnderecoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

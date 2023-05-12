from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from .views import ContatoViewSet, GrupoViewSet


router = DefaultRouter()
router.register(r'contatos', ContatoViewSet)
router.register(r'grupos', GrupoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

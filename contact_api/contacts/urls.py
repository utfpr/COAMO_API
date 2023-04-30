from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from .views import ContatoViewSet


router = DefaultRouter()
router.register(r'contatos', ContatoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

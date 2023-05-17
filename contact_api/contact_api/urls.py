from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('contacts.urls')),
    # obtenção do token JWT
    path('token/', TokenObtainPairView.as_view(), name='token_pair'),
    # atualizar o token JWT
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

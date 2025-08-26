"""
URL configuration for Tienda_backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.http import JsonResponse

# Vista simple para la raíz
def root_view(request):
    return JsonResponse({"message": "Bienvenido a la API de Tienda!"})

urlpatterns = [
    path('', root_view),  # raíz
    path('admin/', admin.site.urls),  # panel de administración
    path('api/', include('Tienda_app.urls')),  # endpoints CRUD
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # obtener token
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # renovar token
]

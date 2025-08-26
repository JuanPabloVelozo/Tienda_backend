from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    MarcaViewSet, CategoriaViewSet, ProductoViewSet, ProductoImagenViewSet,
    DireccionEnvioViewSet, OrdenViewSet, DetalleOrdenViewSet, ResenaViewSet
)

router = DefaultRouter()
router.register(r'marcas', MarcaViewSet)
router.register(r'categorias', CategoriaViewSet)
router.register(r'productos', ProductoViewSet)
router.register(r'productos-imagenes', ProductoImagenViewSet)
router.register(r'direcciones', DireccionEnvioViewSet)
router.register(r'ordenes', OrdenViewSet)
router.register(r'detalles-orden', DetalleOrdenViewSet)
router.register(r'resenas', ResenaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

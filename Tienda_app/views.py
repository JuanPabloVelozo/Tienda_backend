from rest_framework import viewsets
from .models import Marca, Categoria, Producto, ProductoImagen, DireccionEnvio, Orden, DetalleOrden, Resena
from .serializers import (
    MarcaSerializer, CategoriaSerializer, ProductoSerializer,
    ProductoImagenSerializer, DireccionEnvioSerializer,
    OrdenSerializer, DetalleOrdenSerializer, ResenaSerializer
)

class MarcaViewSet(viewsets.ModelViewSet):
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

class ProductoImagenViewSet(viewsets.ModelViewSet):
    queryset = ProductoImagen.objects.all()
    serializer_class = ProductoImagenSerializer

class DireccionEnvioViewSet(viewsets.ModelViewSet):
    queryset = DireccionEnvio.objects.all()
    serializer_class = DireccionEnvioSerializer

class OrdenViewSet(viewsets.ModelViewSet):
    queryset = Orden.objects.all()
    serializer_class = OrdenSerializer

class DetalleOrdenViewSet(viewsets.ModelViewSet):
    queryset = DetalleOrden.objects.all()
    serializer_class = DetalleOrdenSerializer

class ResenaViewSet(viewsets.ModelViewSet):
    queryset = Resena.objects.all()
    serializer_class = ResenaSerializer

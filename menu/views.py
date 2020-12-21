from rest_framework import viewsets
from .serializers import CategorySerializer, ProductSerializer
from .models import Category, Product


class MenuView(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

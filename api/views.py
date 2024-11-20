
from rest_framework import viewsets
from .models import Category,Product,Order,HomeVideo,AdminProfile
from .serializers import CatalogSerializer,ProductSerializer,OrderSerializer,HomeVideoSerializer,AdminProfileSerializer
from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
# Create your views here.

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CatalogSerializer

# class ProductViewSet(viewsets.ModelViewSet):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
    
class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    
class AdminProfileViewSet(viewsets.ModelViewSet):
    queryset = AdminProfile.objects.all()
    serializer_class = AdminProfileSerializer


# class HomeVideoViewSet(viewsets.ModelViewSet):
#     queryset = HomeVideo.objects.filter(is_active=True)
#     serializer_class = HomeVideoSerializer
    
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # permission_classes = [IsAuthenticated]

class HomeVideoViewSet(viewsets.ModelViewSet):
    queryset = HomeVideo.objects.all()
    serializer_class = HomeVideoSerializer
    # permission_classes = [IsAuthenticated]
from rest_framework import serializers
from .models import Category,Product,Order,HomeVideo,AdminProfile
from django.contrib.auth.models import User


class CatalogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','name','description']

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id','category','name','price','image']

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'full_name', 'phone_number', 'created_at']

class HomeVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeVideo
        fields = ['id','video','is_active']
        

class AdminProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username')  # Agar username kerak bo'lsa

    class Meta:
        model = AdminProfile
        fields = ['username', 'is_superadmin', 'phone_number']  # AdminProfile'da mavjud bo'lgan maydonlarni qo'shing

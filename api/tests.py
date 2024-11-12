from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Product, Category

class ProductAPITestCase(APITestCase):
    
    def setUp(self):
        # Test uchun kategoriya va mahsulot yaratamiz
        self.category = Category.objects.create(name="Test Category", description="Test description")
        self.product_data = {
            "name": "Test Product",
            "price": "99.99",
            "category": self.category.id,
        }
        self.url = reverse('product-list')  # Bu URL routerga bog‘langan bo‘lishi kerak

        # Foydalanuvchini yaratamiz va uni autentifikatsiya qilamiz
        self.user = User.objects.create_user(username="testuser", password="testpassword")
        self.client.force_authenticate(user=self.user)

    def test_create_product(self):
        response = self.client.post(self.url, self.product_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_product_list(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_product(self):
        # Mahsulotni dastlab yaratamiz
        product = Product.objects.create(name="Old Product", price="50.00", category=self.category)
        url = reverse('product-detail', args=[product.id])
        
        updated_data = {"name": "Updated Product", "price": "89.99", "category": self.category.id}
        response = self.client.put(url, updated_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_delete_product(self):
        # Mahsulotni dastlab yaratamiz
        product = Product.objects.create(name="Old Product", price="50.00", category=self.category)
        url = reverse('product-detail', args=[product.id])
        
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

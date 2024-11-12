from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True,null=True)
    
    
    def __str__(self):
        return self.name
    

class Product(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name='products')
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    image = models.ImageField(upload_to='products_image/')
    
    def __str__(self) -> str:
        return self.name
    
class HomeVideo(models.Model):
    video = models.FileField(upload_to='home_video/')
    is_active = models.BooleanField(default=True)
    
    def save(self,*args,**kwargs) -> None:
        if not self.pk and HomeVideo.objects.filter(is_active = True).exists():
            HomeVideo.objects.update(is_active=False)
        super().save(*args,**kwargs)
    
    def __str__(self) -> str:
        return f"Home video: {'Active' if self.is_active else 'Inactive'}"

class Order(models.Model):
    full_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return f'zaqaz {self.first_name} {self.last_name} on {self.created_at}'



class AdminProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='admin_profiles')
    is_superadmin = models.BooleanField(default=False)
    phone_number = models.CharField(max_length=20,blank=True,null=True)
    def __str__(self):
        return f"Admin Profile: {self.user.username}"
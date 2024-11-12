from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import AdminProfile

@receiver(post_save, sender=User)
def create_admin_profile(sender,instance,created,**kwargs):
    if created:
        AdminProfile.objects.create(user=instance)
        
# @receiver(post_save,sender=User)
# def save_admin_profile(sender,instance,**kwargs):
#     instance.admin_profile.save()

@receiver(post_save, sender=User)
def save_admin_profile(sender, instance, **kwargs):
    if hasattr(instance, 'admin_profiles'):  # admin_profile o‘rniga admin_profiles ni ishlating
        instance.admin_profiles.save()
    else:
        AdminProfile.objects.create(user=instance)  # Yangi profil yarating
        
        
# key a28d199dfcfb7d2726db99ea48f44872342437a2
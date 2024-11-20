from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import AdminProfile
import requests
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Order  # Order model nomi bilan almashtiring

@receiver(post_save, sender=Order)
def send_order_notification(sender, instance, created, **kwargs):
    if created:
        
        bot_token = '7823484496:AAGX_0Q49tSjSoGHJq9Ntsf7iNkiylkncII'
        chat_id = '1267900230'
        message = f"Yangi buyurtma qabul qilindi!\nIsm: {instance.full_name}\nTelefon: {instance.phone_number}\nVaqt: {str(instance.created_at)[:-13]}"

        url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
        payload = {
            'chat_id': chat_id,
            'text': message
        }

        # Xabar yuborish
        try:
            requests.post(url, data=payload)
        except Exception as e:
            print("Xabar yuborilmadi:", e)




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
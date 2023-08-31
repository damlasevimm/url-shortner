from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import *


@receiver(post_save, sender=URL, dispatch_uid="add_new_hit")
def add_new_hit(sender, instance, **kwargs):
    URLHit.objects.create(url_id=instance.id)
    print("test")
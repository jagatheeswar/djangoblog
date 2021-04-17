from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile, Userdetails, Phonenumbers


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()

@receiver(post_save, sender=User)
def create_userdetails(sender, instance, created, **kwargs):
    if created:
        Userdetails.objects.create(user=instance, dropcountry="IN")


@receiver(post_save, sender=User)
def save_userdetails(sender, instance, **kwargs):
    instance.userdetails.save()    


@receiver(post_save, sender=User)
def create_phonenumbers(sender, instance, created, **kwargs):
    if created:
        Phonenumbers.objects.create(user=instance, mobileno="0", day="01", month="january")


@receiver(post_save, sender=User)
def save_phonenumbers(sender, instance, **kwargs):
    instance.phonenumbers.save()    
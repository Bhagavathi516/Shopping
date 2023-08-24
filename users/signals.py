from django.db.models.signals import post_save, pre_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import UserProfile

@receiver(pre_save, sender=User)
def pre_save_receiver(sender, instance, **kwargs):
    """
    Signal receiver to print the current state of the object before saving.
    """
    print("...............")
    print("Pre-Save Signal Triggered for:", instance)
    print("state:", instance._state)
    print("sender:", sender)
    print("Current state before saving:")
    print(instance.__dict__)
    print("...............")

@receiver(post_save, sender=User )
def create_profile(sender, instance, created, **kwargs):
    """
    Signal receiver to print the current state of the object after saving.
    """
    if created:
        print("User is created")
        UserProfile.objects.create(user=instance)
        print("Userprofile is also created.")
    else:
        print("User and UserProfile are updated")
    # print("created:", created)
    print("Post-Save Signal Triggered for:", instance)
    print("state:", instance._state)
    print("sender:", sender)
    print("username:", instance.username)
    print("email id:", instance.email)
    print('is superuser:', instance.is_superuser)
    # print("name:", instance.userprofile.name)
    # print("phone_number:", instance.userprofile.phone_number)
    # print("place:", instance.userprofile.place)
    print("...............")
    # print(instance.__dict__)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.userprofile.save()

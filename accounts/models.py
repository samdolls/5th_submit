from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    followings = models.ManyToManyField("self", related_name = "followers", symmetrical = False)
    nickname = models.CharField(max_length = 50)
    favorite = models.CharField(max_length = 100, blank = True)
    animal = models.TextField(max_length = 100, blank = True)


# @receiver(post_save, sender = User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user = instance)

# @receiver(post_save, sender = User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()
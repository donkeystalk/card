from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.dispatch import receiver
from django.conf import settings

class Address(models.Model):
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	address1 = models.CharField(max_length=50)
	address2 = models.CharField(max_length=50, null=True, blank=True)
	city = models.CharField(max_length=50)
	state = models.CharField(max_length=50)
	zip_code = models.CharField(max_length=50)

class UserProfile(models.Model):
	user = models.OneToOneField(User)
	shipping = models.OneToOneField(Address, related_name='shipping', null=True)
	billing = models.OneToOneField(Address, related_name='billing')

@receiver(user_logged_in)
def login_set_profile(sender, **kwargs):
	user = kwargs['user']
	up = UserProfile.objects.get(user=user)
	kwargs['request'].session[settings.USER_PROFILE_KEY] = up

@receiver(user_logged_out)
def logout_clear_profile(sender, **kwargs):
	kwargs['request'].session[settings.USER_PROFILE_KEY] = None

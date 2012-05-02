from django.db import models
from django.contrib.auth.models import User

class Address(models.Model):
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	address1 = models.CharField(max_length=50)
	address2 = models.CharField(max_length=50)
	city = models.CharField(max_length=50)
	state = models.CharField(max_length=50)
	zip_code = models.CharField(max_length=50)

class UserProfile(models.Model):
	user = models.OneToOneField(User)
	shipping = models.OneToOneField(Address, related_name='shipping')
	billing = models.OneToOneField(Address, related_name='billing')
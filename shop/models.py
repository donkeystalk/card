from django.db import models
from userprofile.models import UserProfile
import datetime

# Create your models here.
class Item(models.Model):
	name = models.CharField(max_length=50)
	description = models.TextField(blank=True)
	onHand = models.IntegerField(default=0)
	price = models.FloatField(default=0.0)

class LineItem(models.Model):
	item = models.ForeignKey('Item', unique=False)
	quantity = models.IntegerField(default=0)
	order = models.ForeignKey('Order', null=True)

class Order(models.Model):
	created = models.DateField(default=datetime.datetime.now())
	userProfile = models.ForeignKey(UserProfile, unique=False)
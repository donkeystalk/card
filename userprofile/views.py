from django.shortcuts import render_to_response, redirect
from shop.models import Item, LineItem, Order
from models import UserProfile
from django.contrib.auth.models import User
from django.http import Http404
from django.conf import settings
from django.template import RequestContext
from django.contrib.auth.decorators import login_required

import logging


@login_required
def view_orders(request):
	user_profile = request.session[settings.USER_PROFILE_KEY]
	orders = Order.objects.filter(userProfile=user_profile)
	return render_to_response('orders.html', {'orders':orders}, context_instance=RequestContext(request))

@login_required
def view_individual_order(request, orderId):
	user_profile = UserProfile.objects.get(user=request.user)
	
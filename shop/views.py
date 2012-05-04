from django.shortcuts import render_to_response, redirect
from models import Item, LineItem, Order
from userprofile.models import UserProfile
from django.http import Http404
from django.conf import settings
from django.template import RequestContext
from utils import line_items_from_cart, update_cart_with_list_line_item

import logging
from django.contrib.auth.decorators import login_required


logger = logging.getLogger('card.shop.views')

def index(request):
	items = Item.objects.all()
	return render_to_response('index.html', {'items':items})

def item(request, itemId):
	try:
		item = Item.objects.get(pk=itemId)
	except Item.DoesNotExist:
		item = None
	return render_to_response('item_detail.html', {'item' : item})

def view_cart(request):
	items = line_items_from_cart(request)
	return render_to_response('cart.html', 
							  {'items' : items},
							  context_instance=RequestContext(request))

@login_required
def checkout(request):
	quantityChanged = False
	userProfile = UserProfile.objects.get(user=request.user)
	if not request.session.get(settings.CART_KEY):
		return redirect('/shop/cart')
	lineItems = line_items_from_cart(request)
	for li in lineItems:
		li.item = Item.objects.get(pk=li.item_id)
		if li.item.onHand < li.quantity:
			quantityChanged = True
			li.quantity = li.item.onHand
			request.flash[li.item.name] = 'Quantity on hand for %s is less than ordered, order changed to the number on hand.' % li.item.name
	if quantityChanged:
		request = update_cart_with_list_line_item(request, lineItems)
		return redirect('/shop/cart', context_instance=RequestContext(request))
	order = Order(userProfile=userProfile)
	order.save()
	for li in lineItems:
		li_save = LineItem(order=order,item=li.item, quantity=li.quantity)
		li_save.save()
		update_item = Item.objects.get(pk=li.item.id)
		update_item.onHand -= li.quantity
		update_item.save()
	request.session[settings.CART_KEY] = None
	return render_to_response('checkout.html', {'order': order})


def add(request, itemId):
	if not request.session.get(settings.CART_KEY):
		request.session[settings.CART_KEY] = {}
	cart = request.session[settings.CART_KEY]
	try:
		item = Item.objects.get(pk=itemId)
		if item.onHand <= 0:
			request.flash['message'] = 'Item %s is out of stock.' % item.name
			return redirect('/shop/cart', context_instance=RequestContext(request))
		if itemId in cart:
			logger.info('adding 1 to quantity %s' % cart[itemId].quantity)
			cart[itemId].quantity += 1
			logger.info('quantity %s' % request.session[settings.CART_KEY][itemId].quantity)
		else:
			cart[itemId] = LineItem(item=item, quantity=1, order=None)
	except Item.DoesNotExist:
		request.flash['message'] = 'Item %s added does not exist, please select a different item.' % itemId
	request.session[settings.CART_KEY] = cart
	return redirect('/shop/cart', context_instance=RequestContext(request))
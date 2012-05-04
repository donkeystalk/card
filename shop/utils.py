from models import LineItem, Item
from django.conf import settings

def line_items_from_cart(request):
	retVal = []
	cart = request.session.get(settings.CART_KEY)
	if cart:
		for itemId in cart:
			li = cart[itemId]
			li.item = Item.objects.get(pk=itemId)
			retVal.append(li)
	return retVal

def update_cart_with_list_line_item(request, items):
	cart = {}
	if items:
		for li in items:
			cart[li.item_id] = li
		request.session[settings.CART_KEY] = cart
	return request
	
from django.shortcuts import render_to_response
from models import Item
from django.http import Http404
from django.contrib.auth.decorators import login_required

def index(request):
	items = Item.objects.all()
	return render_to_response('index.html', {'items':items})

@login_required
def item(request, itemId):
	try:
		item = Item.objects.get(pk=itemId)
	except Item.DoesNotExist:
		item = None
	return render_to_response('item_detail.html', {'item' : item})
from django.shortcuts import render_to_response, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from userprofile.forms import AddressForm
from django.template import RequestContext
from django.core.exceptions import ValidationError
from userprofile.models import UserProfile
from django.contrib.auth import authenticate, login
import logging

logger = logging.getLogger('card.userprofile.views')

def auth_login(request):
	login_form = AuthenticationForm()
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				login(request, user)
				if 'next' in request.POST:
					return redirect(request.POST['next'])
				else:
					return redirect('/')
		else:
			request.flash['message'] = 'User %s does not exist. Please register.' % username
			return redirect('/register')
	return render_to_response('login.html',
							  {'login_form':login_form},
							  context_instance=RequestContext(request))

def register(request):
	user_form = UserCreationForm(prefix='user')
	billing_form = AddressForm(prefix='billing')
	if request.method == 'POST':
		user_form = UserCreationForm(data=request.POST, prefix='user')
		billing_form = AddressForm(data=request.POST, prefix='billing')
		if user_form.is_valid() and billing_form.is_valid():
			user = user_form.save()
			billing = billing_form.save()
			up = UserProfile(user=user, billing=billing)
			up.save()
			request.flash['message'] = 'Thanks for registering %s' % user.username
			return redirect('/login')
	return render_to_response('register.html', 
							  {'user_form' : user_form, 'billing_form' : billing_form},
							  context_instance=RequestContext(request))
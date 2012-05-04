from django.conf.urls import patterns, include, url
from shop import urls

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
	#url(r'^$', )
    # Examples:
    # url(r'^$', 'card.views.home', name='home'),
    (r'^$','shop.views.index'),
    (r'cart', 'shop.views.view_cart'),
    (r'checkout', 'shop.views.checkout'),
    url(r'^shop/', include('shop.urls')),
    url(r'^register/', 'card.views.register'),
    url(r'^login/', 'card.views.auth_login'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)

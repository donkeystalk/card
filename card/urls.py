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
    (r'logout', 'card.views.auth_logout'),
    url(r'^shop/', include('shop.urls')),
    url(r'^register/', 'card.views.register'),
    url(r'^login/', 'card.views.auth_login'),
    url(r'^order', 'userprofile.views.view_orders'),
    url(r'^order/(\d+)', 'userprofile.views.view_individual_order')

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)

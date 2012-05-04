from django.conf.urls import patterns, url, include

urlpatterns = patterns('',
    #(r'^articles/(\d{4})/$', 'news.views.year_archive'),
    # URLs in this file are already prepended with shop/
    # so no slash is needed in front
    (r'^(\d+)/$', 'shop.views.item'),
    (r'^add/(\d+)/$', 'shop.views.add'),
)
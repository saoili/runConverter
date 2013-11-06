from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'runConverter.views.home', name='home'),
    # url(r'^runConverter/', include('runConverter.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^runConverterApp/', include('runConverterApp.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

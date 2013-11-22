from django.conf.urls import patterns, url

from runConverterApp import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index')
)


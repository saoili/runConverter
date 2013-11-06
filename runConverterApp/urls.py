from django.config.urls import patterns, url

from runConverter import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index')
)


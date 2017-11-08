from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^run/$', views.run, name='run'),
    url(r'^progress/$', views.progress, name='progress'),
    url(r'^progress/get/$', views.progressGet, name='progressGet'),
    url(r'^result/$', views.result, name='result'),
]
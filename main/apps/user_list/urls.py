from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^delete/(?P<id>\d+)$', views.delete),
    url(r'^show/(?P<id>\d+)$', views.show),
    url(r'^edit/(?P<id>\d+)$', views.edit),
    url(r'^edit/(?P<id>\d+)/submit$', views.edit_submit),
    url(r'^new$', views.new),
    url(r'^new/submit$', views.new_submit),
    url(r'^$', views.index),
]

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    # url(r'^register_page$', views.register_page),
    # url(r'^register$', views.register),
    # url(r'^login$', views.login),
    # url(r'^dashboard$', views.home),
    # url(r'^userInfo$', views.getInfo),
]

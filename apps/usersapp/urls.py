from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.register),
    url(r'^userInfo$', views.getInfo),
    url(r'^home$', views.home)

]

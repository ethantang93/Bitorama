from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^item$', views.create),
    url(r'^category$', views.createCat),
    url(r'^item/(?P<id>\d+)$', views.itemPage)
]

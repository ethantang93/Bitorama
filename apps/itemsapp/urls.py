from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="item_index"),
    url(r'^create_item$', views.create_item, name="create_item"),
    url(r'^category/(?P<id>\d+)$', views.create_category, name="create_category"),
    url(r'^item/(?P<id>\d+)$', views.item_page),
]

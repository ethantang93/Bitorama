from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^(?P<id>\d+)$', views.get),
    url(r'^create$', views.create),
    url(r'^delete/(?P<id>\d+)$', views.delete),
    url(r'^user/(?P<id>\d+)$', views.getUser),
    url(r'^item/(?P<id>\d+)$', views.getItem),
    url(r'^user/reviews/(?P<id>\d+)$', views.getUserReviews),
    url(r'^item/reviews/(?P<id>\d+)$', views.getItemReviews),
    url(r'^user/transactions/(?P<id>\d+)$', views.getUserTransactions),
    url(r'^item/transactions/(?P<id>\d+)$', views.getItemTransactions),
]

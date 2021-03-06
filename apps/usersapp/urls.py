from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^login_page$', views.login_page),
    url(r'^check_login$', views.check_login, name='check_login'),
    url(r'^login$', views.login, name='login'),
    url(r'^register_page$', views.register_page),
    url(r'^register$', views.register, name='register'),
    url(r'^logout$', views.logout, name='logout'),
    url(r'^dashboard$', views.dashboard),
    url(r'^userInfo$', views.getInfo),
    url(r'^send_message/(?P<sender_id>\d+)/(?P<receiver_id>\d+)$', views.send_message),
    url(r'^del_message/(?P<message_id>\d+)$', views.delete_message),
    url(r'^follow/(?P<follower>\d+)/(?P<followed>\d+)$', views.follow),
    url(r'^unfollow/(?P<follower>\d+)/(?P<followed>\d+)$',views.unfollow)
]

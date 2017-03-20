from django.conf.urls import url
from . import views

# partial_patterns = [

# ]

urlpatterns = [
    url(r'^', views.index),
]

# from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

class User(User):
    # first_name = models.CharField(max_length=30)
    # last_name = models.CharField(max_length=30)
    # email = models.EmailField(max_length=50)
    # password = models.CharField(max_length=255)
    phone = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Address(models.Model):
    street = models.CharField(max_length = 255)
    city = models.CharField(max_length = 255)
    state = models.CharField(max_length = 2)
    zip_code = models.IntegerField()
    apartment_num = models.CharField( max_length = 30)
    address_type = models.IntegerField()
    owners = models.ManyToManyField('User',related_name = 'addresses')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Message(models.Model):
    sender = models.ForeignKey('User',related_name ='message_sent')
    receiver = models.ForeignKey('User',related_name = 'message_received')
    content = models.CharField(max_length=1024)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    subject = models.CharField(max_length=100)

class Connection(models.Model):
    follower = models.ForeignKey('User',related_name = 'is_following')
    followed = models.ForeignKey('User',related_name = 'followed_by')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

from __future__ import unicode_literals

from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from ..usersapp.models import Profile, Address, Message, Connection
from ..itemsapp.models import Item, Tagging, Tag


class Activity(models.Model):
    type_of = models.IntegerField()
    giver = models.ForeignKey('Profile', related_name='activity_giver')
    receiver = models.ForeignKey('Profile', related_name='activity_receiver')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Transaction(models.Model):
    relation = models.ForeignKey('Activity', related_name='transaction_activity')
    bid = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Review(models.Model):
    relation = models.ForeignKey('Activity', related_name='review_activity')
    subject = models.CharField(max_length=50)
    content = models.TextField(max_length=None)
    rating = models.IntegerField(validators=[MaxValueValidator(10), MinValueValidator(1)])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

from __future__ import unicode_literals

from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# # from ..usersapp.models import Profile, Address, Message, Connection
# from ..itemsapp.models import Item, Tagging, Tag
#
#
# class ActivityQuerySet(models.QuerySet):
#     def userid(self, id):
#         return self.filter(owner=id)
#
#     def itemid(self, id):
#         return self.filter(subject=id)
#
#     def transactionid(self, id):
#         # return self.filter(transaction_activity=id)
#         pass
#
# class ActivityManager(models.Manager):
#     def new_activity(self, data):
#         pass
#
# class Activity(models.Model):
#     type_of = models.IntegerField()
#     owner = models.ForeignKey('User', related_name='user_activity')
#     subject = models.ForeignKey('Item', related_name='item_activity')
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#
# class Transaction(models.Model):
#     type_of = models.IntegerField()
#     relation = models.ForeignKey('Activity', related_name='transaction_activity')
#     amount = models.DecimalField(max_digits=10, decimal_places=2)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#
# class Review(models.Model):
#     relation = models.ForeignKey('Activity', related_name='review_activity')
#     subject = models.CharField(max_length=50)
#     content = models.TextField(max_length=None)
#     rating = models.IntegerField(validators=[MaxValueValidator(10), MinValueValidator(1)])
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

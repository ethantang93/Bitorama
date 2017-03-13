from __future__ import unicode_literals

from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from ..usersapp.models import User
from ..itemsapp.models import Item


class ActivityQuerySet(models.QuerySet):
    def userid(self, id):
        return self.filter(owner=id)

    def itemid(self, id):
        return self.filter(subject=id)

    def transactionid(self, id):
        # return self.filter(transaction_activity=id)
        pass

class ActivityManager(models.Manager):
    def get_queryset(self):
        return ActivityQuerySet(self.model, using=self._db)

    def new_activity(self, data):
        if data.type == 'transaction':
            newActivity = Activity(data.activity)
            newActivity.save()
            newTransaction = Transaction(data.transaction)
            newTransaction.save()
        elif data.type == 'review':
            newReview = Review(data.review)
            newReview.save()

    def get_user(self, id):
        return self.get_queryset().userid(id)

class Activity(models.Model):
    owner = models.ForeignKey(User, related_name='user_activity')
    subject = models.ForeignKey(Item, related_name='item_activity')
    type_of = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ActivityManager()

class Transaction(models.Model):
    relation = models.ForeignKey(Activity, related_name='transaction_activity')
    type_of = models.IntegerField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Review(models.Model):
    relation = models.ForeignKey(Activity, related_name='review_activity')
    subject = models.CharField(max_length=50)
    content = models.TextField(max_length=None)
    rating = models.IntegerField(validators=[MaxValueValidator(10), MinValueValidator(1)])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

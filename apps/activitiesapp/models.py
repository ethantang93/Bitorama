from __future__ import unicode_literals

from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from ..itemsapp.models import Item
from ..usersapp.models import Address, Profile


class ActivityQuerySet(models.QuerySet):
    def userid(self, id):
        return self.filter(owner=id)

    def itemid(self, id):
        return self.filter(target=id)

class ActivityManager(models.Manager):
    def get_queryset(self):
        return TransactionQuerySet(self.model, using=self._db)

    def by_user(self, id):
        return self.get_queryset().userid(id)

    def by_item(self, id):
        return self.get_queryset().itemid(id)

class TransactionQuerySet(ActivityQuerySet):
    def winning(self):
        return self.get_queryset().filter(type_of=1)

class TransactionManager(ActivityManager):
    def get_queryset(self):
        return TransactionQuerySet(self.model, using=self._db)

    def create(self, data):
        newTransaction = Transaction(data)
        newTransaction.save()
        return newTransaction

    def winning_bid(self, user=False, item=False):
        result = Transaction.winning()
        if user:
            result = result.by_user(user)
        if item:
            result = result.by_item(item)
        return result

class ReviewQuerySet(ActivityQuerySet):
    def rating_gt(self, rating):
        return self.filter(rating__gt=rating)

class ReviewManager(models.Manager):
    def get_queryset(self):
        return ReviewQuerySet(self.model, using=self._db)

    def create(self, data):
        newReview = Review(data.review)
        newReview.save()
        return newReview

    def by_rating(self, rating):
        return self.get_queryset().rating_gt(rating)

    def by_user(self, id):
        return self.get_queryset().userid(id)

    def by_item(self, id):
        return self.get_queryset().itemid(id)

class Transaction(models.Model):
    owner = models.ForeignKey(Profile, related_name='bidder')
    target = models.ForeignKey(Item, related_name='bid')
    address = models.ForeignKey(Address, blank=True, null=True, related_name='shipping')
    type_of = models.IntegerField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = TransactionManager()

    def as_dict(self):
        return {
            'id': self.id,
            'owner_id': self.owner_id,
            'target_id': self.target_id,
            'address_id': self.address_id,
            'type_of': self.type_of,
            'amount': self.amount,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }

class Review(models.Model):
    owner = models.ForeignKey(Profile, related_name='reviewer')
    target = models.ForeignKey(Item, related_name='reviewed')
    subject = models.CharField(max_length=50)
    content = models.TextField(max_length=None)
    rating = models.IntegerField(validators=[MaxValueValidator(10), MinValueValidator(1)])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ReviewManager()

    def as_dict(self):
        return {
            'id': self.id,
            'owner_id': self.owner_id,
            'target_id': self.target_id,
            'subject': self.subject,
            'content': self.content,
            'rating': self.rating,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }

# class Activity(models.Model):
#     owner = models.ForeignKey(Profile, related_name='user_activity')
#     subject = models.ForeignKey(Item, related_name='item_activity')
#     type_of = models.IntegerField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     objects = ActivityManager()

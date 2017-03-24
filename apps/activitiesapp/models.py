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
        return self.filter(type_of=1)

class TransactionManager(ActivityManager):
    def get_queryset(self):
        return TransactionQuerySet(self.model, using=self._db)

    def winning_bid(self, user=False, item=False):
        result = self.get_queryset().winning()
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

class Review(models.Model):
    owner = models.ForeignKey(Profile, related_name='reviewer')
    target = models.ForeignKey(Item, related_name='reviewed')
    subject = models.CharField(max_length=50)
    content = models.TextField(max_length=None)
    rating = models.IntegerField(validators=[MaxValueValidator(10), MinValueValidator(1)])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ReviewManager()


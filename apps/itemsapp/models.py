from __future__ import unicode_literals
from django.db import models

class ItemManager(models.Manager):
    def sellItem(self,request):
        # if !description
        # item = self.create(description=request.POST['description'],item_name=request.post['item_name'])
        # return(item)
        pass


# Create your models here.
class Item(models.Model):
    item_name = models.CharField(max_length = 255)
    price = models.IntegerField()
    views = models.IntegerField()
    description = models.CharField(max_length = 255)
    comments = models.CharField(max_length = 255)
    seller = models.CharField(max_length = 50)
    quantity = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Tagging(models.Model):
    item = models.ForeignKey('Item', related_name="taggings")
    category = models.ForeignKey('Tag', related_name="taggin_1")
    sub_category = models.ForeignKey('Tag', related_name="taggin_2")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Tag(models.Model):
    name = models.CharField(max_length = 50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

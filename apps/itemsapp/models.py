from __future__ import unicode_literals
from django.db import models

# class ItemManager(models.Manager):
#     def sellItem(self,request):
#         if !description
#         item = self.create(description=request.POST['description'],item_name=request.post['item_name'])
#         return(item)


# Create your models here.
# class Item(models.model):
#     item_name = models.CharField(max_length = 255)
#     price = models.IntegerField(max_length = 6)
#     views = models.IntegerField(max_length = 255)
#     description = models.CharField(max_length = 255)
#     comments = models.CharField(max_length = 255)
#     seller = models.Charfiled(max_length = 50)
#     quantity = models.IntegerField(max_length = 255)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#
# class Tagging(models.model):
#     category = models.ForeignKey('Tag', related_name = "")
#     subCategory = models.ForeignKey('Tag', related_name = "")
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#
#
# class Tag(models.model):
#     category = models..Charfiled(max_length = 50)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
class Item(models.Model):
    pass
class Tagging(models.Model):
    pass
class Tag(models.Model):
    pass

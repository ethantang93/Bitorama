from __future__ import unicode_literals
from django.db import models
from ..usersapp.models import Profile

class ItemManager(models.Manager):
    def sellItem(self,request):
        item = self.create(description=request.POST['description'],item_name=request.post['item_name'])
        return(item)

class Item(models.Model):
    item_name = models.CharField(max_length = 255)
    price = models.IntegerField()
    views = models.IntegerField()
    description = models.CharField(max_length = 255)
    seller = models.ForeignKey(Profile, related_name="sold_items")
    quantity = models.IntegerField()
    tags = models.ManyToManyField('Tag', related_name="items")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ItemManager()

class Tag(models.Model):
    parent = models.ForeignKey('self', related_name="children", blank=True, null=True)
    name = models.CharField(max_length = 50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def get_items(self):
        results = self.items
        for child in children:
            child_results = child.getItems()
            results |= child_results
    def get_path_string(self):
        if (self.parent):
            return self.parent.get_path_string() + " > " + self.name
        else:
            return self.name
    def get_path(self):
        if (self.parent):
            return self.parent.get_path() + [self.id]
        else:
            return [self.id]

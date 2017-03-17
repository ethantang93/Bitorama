from __future__ import unicode_literals
from django.db import models
from ..usersapp.models import Profile


class ItemManager(models.Manager):
    def makeItem(self,request):
        print 'item Manager'
        userid = request.session['user']['id']
        print userid
        # createTag = Tag(name=request.POST['category']).save()
        userObj = Profile.objects.get(id = userid)
        print userObj
        createdItem = Item(item_name = request.POST['item'],price = request.POST['price'],views= 1, description = request.POST['description'], seller= userObj, tag_id= request.POST['category'] ).save()
        return


# Create your models here.
class Item(models.Model):
    item_name = models.CharField(max_length = 255, blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    views = models.IntegerField(blank=True, null=True)
    description = models.CharField(max_length = 255, blank=True, null=True)
    seller = models.ForeignKey(Profile, related_name="sold_items", blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)
    tag = models.ForeignKey('Tag', related_name="items", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ItemManager()

class TagManager(models.Manager):
    def getTagList(self, blank=False):
        roots = self.filter(parent=None)
        html = "<select name='category'>\n"
        if blank:
            html += "<option value='-----'>None</option>"
        for root in roots:
            html += root.buildChildTagSelect(0)
        html += "</select>"
        return html

class Tag(models.Model):
    parent = models.ForeignKey('self', related_name="children", blank=True, null=True)
    name = models.CharField(max_length = 50, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = TagManager()
    def get_items(self):
        results = self.items
        for child in self.children.all():
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
    def buildChildTagSelect(self, indent):
        html = "<option value="+str(self.id)+">"+("&#160;"*indent)+self.name+"</option>\n"
        for child in self.children.all():
            html += child.buildChildTagSelect(indent+1)
        return html

import django
from apps.itemsapp.models import *

django.setup()
item=Item.objects.create(item_name='computer', price=500, views=0, description='cool computer man', comments='this is a comment',seller='luis',quantity=100)

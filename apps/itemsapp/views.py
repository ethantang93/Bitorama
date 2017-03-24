from django.shortcuts import render, redirect
from models import Item, Tag
import json
from django.http import JsonResponse

# Create your views here.
def index(request):
    items = Item.objects.all()
    context = {
        'allItems': items,
        "tags":Tag.objects.getTagList()
    }
    return render(request, 'bitorama/itemsPage.html', context)

def create_item(request):
    # tag = Tag.objects.get(id=4)
    # Tag.get_items(tag)
    data = json.loads(request.body)
    item = Item.objects.create_item(data)
    if item[0]:
        return JsonResponse({
            'success':True,
            'item':item[1]
        })
    else:
        return JsonResponse({
            'success':False,
            'item':None
        })
def create_category(request,id):
    if request.POST['category']=='-----':
        parent = None
    else:
        parent = request.POST['category']
    cat = Tag.objects.create(name = request.POST['name'],parent_id=parent)
    return redirect('/products')

def itemPage(request,id):
    item = Item.objects.get(id = id)
    context = {
        'itemDetails': item,
        'tags':Tag.objects.getTagList(True)
    }
    return render(request, 'bitorama/details.html', context)

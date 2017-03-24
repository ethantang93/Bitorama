from django.shortcuts import render, redirect
from models import Item, Tag
import json
from django.http import JsonResponse
from django.forms.models import model_to_dict

# Create your views here.


def index(request):
    items = Item.objects.all()
    json_items = [model_to_dict(item) for item in items]
    context = {
        'items': json_items,
        # "tags": Tag.objects.get_tag_list()
    }
    return JsonResponse(context)


def create_item(request):
    # tag = Tag.objects.get(id=4)
    # Tag.get_items(tag)
    data = json.loads(request.body)
    item = Item.objects.create_item(data)
    if item[0]:
        return JsonResponse({
            'success': True,
            'item': item[1]
        })
    else:
        return JsonResponse({
            'success': False,
            'item': None
        })


def create_category(request, id):
    if request.POST['category']=='-----':
        parent = None
    else:
        parent = request.POST['category']
    cat = Tag.objects.create(name=request.POST['name'], parent_id=parent)
    return redirect('/products')


def item_page(request, id):
    item = Item.objects.get(id=id)
    context = {
        'itemDetails': item,
        'tags': Tag.objects.get_tag_list(True)
    }
    return render(request, 'bitorama/details.html', context)

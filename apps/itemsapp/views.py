from django.shortcuts import render, redirect
from models import Item, Tag

# Create your views here.
def index(request):
    items = Item.objects.all()
    context = {
        'allItems': items,
        "tags":Tag.objects.getTagList()
    }
    return render(request, 'bitorama/itemsPage.html', context)

def create(request):
    returnData = Item.objects.makeItem(request)
    # print request.session['user'].get('username')
    return redirect('/products')
def createCat(request,id):
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

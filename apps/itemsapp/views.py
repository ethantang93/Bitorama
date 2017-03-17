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
def createCat(request):
    Tag.Objects.create(name = request.POST['category'])
    return redirect('/products')

def itemPage(request,id):
    item = Item.objects.get(id = id)
    print item
    return render(request, 'bitorama/details.html')

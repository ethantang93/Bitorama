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
    print request.POST['mainCat']
    cat = Tag.objects.create(name = request.POST['mainCat'],parent=None)
    request.session['categoryId'] = cat.id
    itemObj = Item.objects.get(id = id)
    print request.session['categoryId']
    catObj = Tag.objects.filter(id=request.session['categoryId'])
    print catObj
    itemObj.tags = catObj
    itemObj.save()
    print itemObj.tags
    return redirect('/products')

def itemPage(request,id):
    item = Item.objects.get(id = id)
    context = {
        'itemDetails': item
    }
    return render(request, 'bitorama/details.html', context)

def subCat(request):
    mainCatObj = Tag.objects.get(id=request.session['categoryId'])
    Tag.objects.create(name = request.POST['subCat'], parent=mainCatObj)
    return redirect('/products')

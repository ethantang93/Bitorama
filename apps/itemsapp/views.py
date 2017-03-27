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
    print request.POST['category']
    # print request.session['user'].get('username')
    return redirect('/products')
def createCat(request):
    if request.POST['category']=='-----':
        parent = None
    else:
        parent = request.POST['category']
        print '1111111111111111111111111S'
        print parent
    cat = Tag.objects.create(name = request.POST['name'],parent_id=parent)
    return redirect('/products')
def updateCat(request,id):
    item = Item.objects.get(id = id)
    print item.tag_id
    tag =Tag.objects.create(name = request.POST['name'],parent_id=item.tag_id)
    item.tag_id = tag.id
    item.save()
    print '100'*30
    print item.tag_id
    print '100'*30
    return redirect('/products/item/' + id)


def itemPage(request,id):
    item = Item.objects.get(id = id)
    print item.tag_id, 'tag ID heree'
    tag = Tag.objects.get(id=item.tag_id)
    query= Tag.get_items(tag)
    for q in query:
        print(q.tag.name)
    print '_________________________________________'
    print item.tag.get_path_string()
    context = {
        'itemDetails': item,
        'tags':Tag.objects.getTagList(True),
        'categories': item.tag.get_path_string()
    }
    return render(request, 'bitorama/details.html', context)

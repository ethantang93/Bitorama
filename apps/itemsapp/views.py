from django.shortcuts import render, redirect
# Create your views here.
<<<<<<< HEAD
def index(request):
    result = Items.objects.sellItem(request)
    return render(request,'bitorama/itemsPage.html')

def create(request):
    print 'in create funtion'
    print request.POST['review']

    return redirect('/products')
=======
def index():
    pass

def getInfo():
    print 'in the get info method'
>>>>>>> d2f50c65b3ccd7577923859ddb74e6912fc0d520

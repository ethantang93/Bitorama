from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    print request
    print 'haiii'
    return render(request,'bitorama/itemsPage.html')

def create(request):
    print 'in create funtion'
    print request.POST['review']

    return redirect('/products')

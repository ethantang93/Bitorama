from django.shortcuts import render, redirect

# Create your views here.
<<<<<<< HEAD
def index(request):
    print request
    print 'haiii'
    return render(request,'bitorama/itemsPage.html')

def create(request):
    print 'in create funtion'
    print request.POST['review']

    return redirect('/products')
=======
def index():
    pass
>>>>>>> e77795c5033a8df598ea1fa7c30e1763ae0141dd

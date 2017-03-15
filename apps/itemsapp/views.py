from django.shortcuts import render, redirect
# Create your views here.
def index(request):
    return render(request, 'bitorama/itemsPage.html')

def create(request):
    returnData = Items.objects.create(request)
    print 'in the get info method'

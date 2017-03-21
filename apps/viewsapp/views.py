from django.shortcuts import render

def index(request):
    print request.session
    return render(request, 'viewsapp/index.html')

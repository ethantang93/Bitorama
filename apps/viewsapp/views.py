from django.shortcuts import render

def index(request):
    # request.session.clear()
    return render(request, 'viewsapp/index.html')

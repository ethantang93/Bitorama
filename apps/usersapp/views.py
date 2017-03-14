from django.shortcuts import render, redirect
from models import Profile
# Create your views here.
def index(request):
    return render(request,'usersapp/index.html')
def register(request):
    username = request.POST['username']
    email = request.POST['email']
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    password = request.POST['password']

    if (Profile.objects.validateReg(request)[0]):
        user = Profile.objects.create_user(username,email,password)
        user.last_name = last_name
        user.first_name = first_name
        user.save()
        return redirect('/admin')

    print("*"*100+"input is not valid")
    return redirect('/users')
def getInfo(request):
    print 'in the getinfo Method'

    return render(request,'usersapp/user.html')

def home(request):
    return render(request, 'usersapp/home.html')

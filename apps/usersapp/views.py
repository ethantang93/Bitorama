from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'usersapp/index.html')

def register_page(request):
    return render(request,'usersapp/register.html')
def dashboard(request):
    return render(request,'usersapp/dashboard.html')

def login(request):
    user = Profile.objects.validateLogin(request)
    if (user[0]):
        login_user(request,user[1])
        return redirect('/users/dashboard')
    print_messages(request,user[1])
    return redirect('/users')

def register(request):
    username = request.POST['username']
    email = request.POST['email']
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    password = request.POST['password']

    user = Profile.objects.validateReg(request)
    if (user[0]):
        user = Profile.objects.create_user(username,email,password)
        user.last_name = last_name
        user.first_name = first_name
        user.save()
        login_user(request,user)
        return redirect('/users/dashboard')

    print("input is not valid")
    print_messages(request,user[1])
    return redirect('/users/register_page')

def login_user(request,user):
    print user
    request.session['user'] = {
    'first_name' : user.first_name,
    'last_name' : user.last_name,
    'username' : user.username,
    'email' : user.email
    }
    # request.session['user'] = user
    return redirect('/dashboard',request)

    print("*"*100+"input is not valid")
    return redirect('/users')

def print_messages(request, message_list):
    for message in message_list:
        messages.add_message(request, messages.INFO, message)

def getInfo(request):
    print 'in the getinfo Method'

    return render(request,'usersapp/user.html')

def home(request):
    return render(request, 'usersapp/home.html')

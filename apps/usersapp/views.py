from django.shortcuts import render, redirect
from models import Profile, Connection, Message, UploadFileForm
from django.contrib import messages
from django.http import HttpResponseRedirect, JsonResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

def index(request):
    users = Profile.objects.all()
    context = {'users': users}
    return render(request, 'usersapp/index.html', context)


def login_page(request):
    return render(request, 'usersapp/login.html')


def register_page(request):
    return render(request, 'usersapp/register.html')


def dashboard(request):
    return render(request, 'usersapp/dashboard.html')

@csrf_exempt
def login(request):
    user = Profile.objects.validateLogin(request)
    return JsonResponse({'data': user})
    # if (user[0]):
    #     login_user(request, user[1])
    #     return redirect('/')
    # print_messages(request, user[1])
    # return redirect('/login_page')


def register(request):
    username = request.POST['username']
    email = request.POST['email']
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    password = request.POST['password']

    user = Profile.objects.validateReg(request)
    if user[0]:
        user = Profile.objects.create_user(username, email, password)
        user.last_name = last_name
        user.first_name = first_name
        user.save()
        login_user(request, user)
        return redirect('/')

    print("input is not valid")
    print_messages(request, user[1])
    return redirect('/register_page')


def login_user(request, user):
    request.session['user'] = {
        'id': user.id,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'username': user.username,
        'email': user.email
    }
    # request.session['user'] = user
    return redirect('/', request)


def logout(request):
    print 'logout in views'
    print request.session
    request.session.pop('user')
    print request.session
    return JsonResponse({'status': True})


def print_messages(request, message_list):
    for message in message_list:
        messages.add_message(request, messages.INFO, message)


def getInfo(request):
    print ('the get info method')

    return render(request, 'usersapp/user.html')


def home(request):
    return render(request, 'usersapp/home.html')


def send_message(request, sender, receiver):
    message = Message.objects.send_message(request, sender, receiver)
    if message[0] is False:
        print_messages(request, message[1])
    return redirect(request, '/dashboard')


def delete_message(request, message_id):
    Message.objects.delete_message(message_id)


def follow(request, follower, followed):
    Connection.objects.follow(follower, followed)
    return redirect('/')

def unfollow(request, follower, followed):
    Connection.objects.unfollow(follower, followed)
    return redirect('/')

import json

from django.contrib import messages
# from django.forms.models import model_to_dict
from django.http import JsonResponse
from django.shortcuts import redirect, render

from models import Connection, Message, Profile, UploadFileForm


# Create your views here.

# def json_user(user):
#     # Convert object to dictionary
#     jsonuser = model_to_dict(user)
#     # Remove password and query set objects from dictionary
#     jsonuser.pop('groups')
#     jsonuser.pop('user_permissions')
#     jsonuser.pop('password')
#     return jsonuser

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

def check_login(request):
    try:
        return JsonResponse({
            'success': True,
            'user': request.session['user']
            })
    except:
        return JsonResponse({
            'success': False,
            'user': None
            })

def login(request):
    user = Profile.objects.validateLogin(request)
    if (user[0]):
        login_user(request, user[1])
        return JsonResponse({
            'success': user[0],
            'user': request.session['user']
            })
    else:
        print_messages(request, user[1])
        return JsonResponse({
            'success': user[0],
            'errors': user[1]
            })

def register(request):
    data = json.loads(request.body)
    username = data['username']
    email = data['email']
    first_name = data['first_name']
    last_name = data['last_name']
    password = data['password']

    user_status = Profile.objects.validateReg(request)
    # jsonuser = model_to_dict(user_status[1])
    if (user_status[0]):
        user = Profile.objects.create_user(username, email, password)
        user.last_name = last_name
        user.first_name = first_name
        user.save()
        login_user(request, user)
        return JsonResponse({
            'success':user_status[0],
            'user': request.session['user']
        })
    # if user[0]:
    #     user = Profile.objects.create_user(username, email, password)
    #     user.last_name = last_name
    #     user.first_name = first_name
    #     user.save()
    #     login_user(request, user)
    #     return redirect('/')
    #
    # print("input is not valid")
    # print_messages(request, user[1])
    # return redirect('/register_page')


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

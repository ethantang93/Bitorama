from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.models import User, UserManager
from django.contrib.auth import authenticate
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')


class ProfileManager(UserManager):
    def validateReg(self, request):
        # check if the inputs are valid
        errors = self.validate_inputs(request)
        if len(errors) > 0:
            return False, errors
        # check if there is an existing username
        try:
            Profile.objects.get(username=request.POST['username'])
            errors.append('user name already exist!')
            return (False, errors)
        except:
            return (True, user)

    def validateLogin(self, request):
        try:
            user = User.objects.get(email=request.POST['email'])
            print request.POST
            # The email matched a record in the database, now test passwords
            password = request.POST['password'].encode()
            if bcrypt.hashpw(password, user.pw_hash.encode()) == user.pw_hash.encode():
                return (True, user)

        except:
            pass
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            return (True, user)
        return (False, ["Email/password don't match."])

    def validate_inputs(self, request):
        errors = []
        if len(request.POST['first_name']) < 2 or len(request.POST['last_name']) < 2:
            errors.append("Please include a first and/or last name longer than two characters.")
        if not EMAIL_REGEX.match(request.POST['email']):
            errors.append("Please include a valid email.")
        if len(request.POST['password']) < 6 or request.POST['password'] != request.POST['confirm_pw']:
            errors.append("Passwords must match and be at least 6 characters.")
        return errors

    def get_all_profiles(self, request):
        # returns all user EXCEPT the current user
        users = Profile.objects.all()
            # .exclude(id=request.session['user']['id'])
        return users


class Profile(User):
    # user = models.OneToOneField(User, on_delete = models.CASCADE)
    phone = models.CharField(max_length=30)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ProfileManager()


class AddressManager(models.Manager):
    def validate_address(self, request):
        errors = []
        if len(request.POST['zip_code']) != 6:
            errors.append("please enter a valid zip code")
        return errors


class Address(models.Model):
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=2)
    zip_code = models.IntegerField()
    apartment_num = models.CharField(max_length=30)
    address_type = models.IntegerField()
    owners = models.ManyToManyField('Profile', related_name='addresses')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = AddressManager()


class MessageManager(models.Manager):
    def validator(self, request):
        errors = []
        if request.POST['receiver'] is None:
            errors.append('must specify a person to send this message to')
        if request.POST['sender'] is None:
            errors.append('must specify a sender of this message')
        if len(request.POST['content']) <= 0:
            errors.append("please don't send a empty message")
        if len(request.POST['subject']) <= 0:
            errors.append('please enter a subject of this message')
        return errors

    def get_user_messages(self, request):
        messages = Message.objects.get(sender=request.POST['sender'])
        return messages

    def send_message(self, request, send_by, send_to):
        errors = self.validator(request)
        if len(errors) > 0:
            return (False, errors)
        # send_by = Profile.objects.get(username = request.POST['sender'])
        # send_to = Profile.objects.get(username = request.POST['receiver'])
        message = self.create(sender=send_by, receiver=send_to, content=request.POST['content'], subject=request.POST['subject'])
        return (True, message)

    def delete_message(self, request, message_id):
        message = Message.objects.get(id=message_id)
        message.delete()
        return ("delete successful")


class Message(models.Model):
    sender = models.ForeignKey('Profile',related_name ='message_sent')
    receiver = models.ForeignKey('Profile',related_name = 'message_received')
    content = models.CharField(max_length=1024)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    subject = models.CharField(max_length=100)
    objects = MessageManager()


class ConnectionManager(models.Manager):
    def follow(self, follower, followed):
        follower = Profile.objects.get(id=follower)
        followed = Profile.objects.get(id=followed)
        connection = self.create(follower=follower, followed=followed)

    def unfollow(self, follower_id, followed_id):
        connection = Connection.objects.get(follower=follower_id, followed=followed_id)
        connection.delete()


class Connection(models.Model):
    follower = models.ForeignKey('Profile', related_name='is_following')
    followed = models.ForeignKey('Profile', related_name='followed_by')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ConnectionManager()

from django import forms
class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()

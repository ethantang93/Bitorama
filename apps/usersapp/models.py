from __future__ import unicode_literals

import json
import re

from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User, UserManager
from django.db import models

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')


class ProfileManager(UserManager):
    def validateReg(self, data):

        # check if the inputs are valid
        errors = self.validate_inputs(data)
        if len(errors) > 0:
            return (False, errors)
        # check if there is an existing username
        try:
            Profile.objects.get(username=data['username'])
            errors.append('user name already exist!')
            return (False, errors)
        except:
            return (True, errors)

    def validateLogin(self, request):
        data = json.loads(request.body)
        user = authenticate(username=data['username'], password=data['password'])
        if user is not None:
            return (True, user)
        else:
            return (False, ["Email/password do not match."])

    def validate_inputs(self, request):
        errors = []
        data = json.loads(request.body)
        if len(data['first_name']) < 2 or len(data['last_name']) < 2:
            errors.append("Please include a first and/or last name longer than two characters.")
        if not EMAIL_REGEX.match(data['email']):
            errors.append("Please include a valid email.")
        if len(data['password']) < 6 or data['password'] != data['confirm_pw']:
            errors.append("Passwords must match and be at least 6 characters.")
        return errors

    def get_all_profiles(self, request):
        # returns all user EXCEPT the current user
        users = Profile.objects.all()
            # .exclude(id=request.session['user']['id'])
        return users
    # def get_conversation(self, sender, receiver):
    #


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
        # if request.POST['receiver'] is None:
        #     errors.append('must specify a person to send this message to')
        # if request.POST['sender'] is None:
        #     errors.append('must specify a sender of this message')
        if len(request.POST['content']) <= 0:
            errors.append("please don't send a empty message")
        # if len(request.POST['subject']) <= 0:
        #     errors.append('please enter a subject of this message')
        return errors

    def get_user_messages(self, request):
        messages = Message.objects.get(sender=request.POST['sender'])
        return messages

    def send_message(self, request, sender_id, receiver_id):
        errors = self.validator(request)
        if len(errors) > 0:
            return (False, errors)
        send_by = Profile.objects.get(id = sender_id)
        send_to = Profile.objects.get(id = receiver_id)
        message = self.create(sender=send_by, receiver=send_to, content=request.POST['content'])
        return (True, message)

    def delete_message(self, request, message_id):
        message = Message.objects.get(id=message_id)
        message.delete()
        return ("delete successful")


class Message(models.Model):
    sender = models.ForeignKey('Profile', related_name='message_sent')
    receiver = models.ForeignKey('Profile', related_name='message_received')
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

class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()

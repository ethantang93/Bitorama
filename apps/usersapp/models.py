from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User,UserManager
from django.db.models.signals import post_save
from django.dispatch import receiver
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

class ProfileManager(UserManager):
    def validateReg(self, request):
        # check if the inputs are valid
        errors = self.validate_inputs(request)
        if len(errors) > 0:
            return (False, errors)
        # check if there is an exsisting username
        try:
            user = User.objects.get(username=request.Post['username'])
            errors.append('user name already exist!')
            return (False, errors)
        except:
            return (True, errors)

    def validateLogin(self, request):
        try:
            user = User.objects.get(email=request.POST['email'])
            print request.POST
            # The email matched a record in the database, now test passwords
            password = request.POST['password'].encode()
            if bcrypt.hashpw(password, user.pw_hash.encode()) == user.pw_hash.encode():
                return (True, user)

        except ObjectDoesNotExist:
            pass

        return (False, ["Email/password don't match."])

    def validate_inputs(self, request):
        errors = []
        if len(request.POST['first_name']) < 2 or len(request.POST['last_name']) < 2:
            errors.append("Please include a first and/or last name longer than two characters.")
        if not EMAIL_REGEX.match(request.POST['email']):
            errors.append("Please include a valid email.")
        if len(request.POST['password']) < 8 or request.POST['password'] != request.POST['confirm_pw']:
            errors.append("Passwords must match and be at least 8 characters.")

        return errors

class Profile(User):
    # user = models.OneToOneField(User, on_delete = models.CASCADE)
    phone = models.CharField(max_length=30)
    updated_at = models.DateTimeField(auto_now=True)

    objects = ProfileManager()

class Address(models.Model):
    street = models.CharField(max_length = 255)
    city = models.CharField(max_length = 255)
    state = models.CharField(max_length = 2)
    zip_code = models.IntegerField()
    apartment_num = models.CharField( max_length = 30)
    address_type = models.IntegerField()
    owners = models.ManyToManyField('Profile',related_name = 'addresses')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Message(models.Model):
    sender = models.ForeignKey('Profile',related_name ='message_sent')
    receiver = models.ForeignKey('Profile',related_name = 'message_received')
    content = models.CharField(max_length=1024)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    subject = models.CharField(max_length=100)

class Connection(models.Model):
    follower = models.ForeignKey('Profile',related_name = 'is_following')
    followed = models.ForeignKey('Profile',related_name = 'followed_by')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

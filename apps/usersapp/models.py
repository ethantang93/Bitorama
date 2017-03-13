from __future__ import unicode_literals

from django.db import models

class User(models.Model):
    first_name = models.charField(max_length=30)
    last_name = models.charField(max_length=30)
    email = models.EmailField(max_length=30)
    phone = models.charField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

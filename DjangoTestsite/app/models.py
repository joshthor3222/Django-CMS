"""
Definition of models.
"""

from django.db import models

# Create your models here.

class ContactSubmission(models.Model):
    name = models.CharField(max_length=128, null=True)
    first_name = models.CharField(max_length=128, null=True)
    last_name = models.CharField(max_length=128, null=True)
    email = models.CharField(max_length=128, unique=True, null=True)
    phone = models.CharField(max_length=24, null=True)
    message = models.TextField(null=True)

class Page(models.Model):
    name = models.CharField(max_length=128, unique=True)
    title = models.CharField(max_length=128)
    url = models.CharField(max_length=128, unique=True)
    createdOn = models.DateTimeField(auto_now_add=True)
    published = models.BooleanField()
    publishedOn = models.DateTimeField()
    lastEditedOn = models.DateTimeField(auto_now=True)
    lastEditedBy = models.CharField(max_length=128)
    metaDescription = models.TextField(null=True)
    parentPage = models.IntegerField()
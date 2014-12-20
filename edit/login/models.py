from django.db import models

# Create your models here.
from django.db import models
from django.forms import ModelForm
from datetime import date
import datetime
from django import forms
from django.forms import Textarea

class notepad(models.Model):
    filename = models.CharField(max_length=50)
    version  = models.CharField(max_length=50)
    content  = models.TextField()
    created  = models.IntegerField(default=0)

    def __str__(self):
        return self.filename;


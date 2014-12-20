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
    author   = models.CharField(max_length=50,default="admin")
    content  = models.TextField()
    created  = models.DateTimeField(default=datetime.datetime.now, blank=True)

    def __str__(self):
        return str( str(self.filename)+ "-"+str(self.content) + "-" + str(self.version) + "-" + str(self.created) + "-" + str(self.author) );

    class Meta:
        get_latest_by = 'created'


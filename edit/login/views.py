# Create your views here.

#views.py
from login.forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
import calendar
import uuid
from login.models import *


@csrf_protect
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password1'],
            email=form.cleaned_data['email']
            )
            return HttpResponseRedirect('register/success/')
    else:
        form = RegistrationForm()
    variables = RequestContext(request, {
    'form': form
    })
 
    return render_to_response(
    'registration/register.html',
    variables,
    )
 
def register_success(request):
    return render_to_response(
    'registration/success.html',
    )
 
def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')
 
@login_required
def home(request):
    return render_to_response(
    'home.html',
    { 'user': request.user }
    )

def search_form(request):
    return render(request, 'registration/search_form.html')

def search(request):
    if 'q' in request.GET:
        message = 'You searched for: %r' % request.GET['q']
    else:
        message = 'You submitted an empty form.'
    return HttpResponse(message)


def creates(request):
    return HttpResponse(uuid.uuid1())

def create_new(request):
    guid = uuid.uuid1();
    to_url=str("http://127.0.0.1:8000/edit/"+str(guid)+"/");
    #q = Question(question_text="What's new?", pub_date=timezone.now())
    dummy=notepad( filename = guid , version=guid , author = request.user ,content="Welcome" , created= datetime.datetime.now() );
    dummy.save();
    return HttpResponseRedirect(to_url);
    

def edit_code(request,file_name):
        form = Postnotepad(request.POST)
        if form.is_valid():
                post = form.save(commit=False)
                post.author = request.user
               # post.created = calendar.timegm(d.utctimetuple());
                post.version = uuid.uuid1();
                post.filename = file_name;
                post.save()

        ret = notepad.objects.filter(filename = file_name).order_by('-created').latest();

        form.filename = file_name;
        form.version = ret.version;
        form.author = ret.author;
        form.content = ret.content;
        form.created = ret.created;
        return render(request, 'registration/create_new.html' ,{'form': form} )            

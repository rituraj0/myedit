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
import os
from subprocess import call
import subprocess
from subprocess import Popen, PIPE, STDOUT
import diff_match_patch



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
        """
        if(request.method == "POST" ):
             return HttpResponse("post")
        if(request.method == "GET" ):    
            return HttpResponse("get")
         
        form = Postnotepad(request.POST)
        """
        if(request.method == "POST" ):
            form = Postnotepad(request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                post.author = request.user
                post.version = uuid.uuid1();
                post.filename = file_name;
                post.save()


        ret = notepad.objects.filter(filename = file_name).order_by('-created').latest();
        form = Postnotepad(instance=ret)
        source_code= ret.content;

        file_name= ret.version+".py";

        file_path = os.path.join( "C:/Users/Rituraj/Documents/GitHub/myedit/files", file_name);
        open_file = open( file_path,"w");
        open_file.write(str(source_code));
        open_file.close()

        cmd = "python "+ file_path;
        p = Popen(cmd, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT)
        output = p.stdout.read()

        changelist = "http://127.0.0.1:8000/changelist/"+str(ret.filename);
      
        return render(request, 'registration/create_new.html' ,{'form': form , 'output':output ,'changelist':changelist} )            

def changelist(request,file_name):
    ret = list(notepad.objects.filter(filename = file_name).order_by('-created'));
    ans = " <h2> Changelist  for  " + file_name  + "  " + " </h2>";
    diff_obj = diff_match_patch.diff_match_patch()

    for i in range ( 1 , len(ret) ):
    
        curr_user = ret[i].author;
        curr_version = ret[i].version;
        curr_time = ret[i].created;
        
        old_string= ret[i-1].content;        
        new_string = ret[i].content;

        diffs = diff_obj.diff_main(old_string, new_string)
        diff_obj.diff_cleanupSemantic(diffs)
        html = diff_obj.diff_prettyHtml(diffs)

        curr_string = "<br><br>  <b> " + " Delta &nbsp " +curr_version + " </b>  ";
        curr_string = curr_string + "  &nbsp  User " + curr_user + " &nbsp Time  " + curr_time.strftime("%d/%m/%Y %H:%M:%S") ;
        curr_string = curr_string + "<br>";
        curr_string = curr_string + html;

        ans = ans + curr_string;
    return HttpResponse( ans )

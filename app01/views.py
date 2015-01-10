from django.shortcuts import render,render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template.context import RequestContext
from django.contrib import auth
from django.contrib import comments
from django.contrib.contenttypes.models import ContentType
import models


# Create your views here.
def acc_login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = auth.authenticate(username=username, password=password)
    print username,'->',password
    
    if user is not None:
        auth.login(request,user)
        content = '''
        Welcome %s !!!
        
        <a href='/logout/' >Logout</a>
        
        '''% user.username
        
        return HttpResponseRedirect('/')
    else:
        return render_to_response('login.html',{'login_err':'Wrong username or password.'})
         
def logout_view(request):
    user = request.user
    auth.logout(request)
    # Redirect to a success page
    return HttpResponse("<b>%s</b> logged out! <br/><a href = '/'>log in again</a>" %user)

def Login(request):
    return render_to_response('login.html')

def index(request):
    bbs_list = models.BBS.objects.all()
    return render_to_response('index.html',{'bbs_list':bbs_list,'user':request.user})

def bbs_detail(request, bbs_id):
    bbs_obj = models.BBS.objects.get(id = bbs_id)
    return render_to_response('bbs_detail.html', {'bbs_obj':bbs_obj}, context_instance = RequestContext(request))

# Write comment to DB
def sub_comment(request):
    print '--->',request.POST
    bbs_id = request.POST.get('bbs_id')
    comment = request.POST.get('comment_content')
    
    # Be careful about the names of the following parameters. 
    # Check django.contrib.contenttypes.models source code if necessary.
    comments.models.Comment.objects.create(
          content_type_id = 7,
          object_pk = bbs_id,   # Not object_id which is very easy to mis-used
          site_id = 1,
          user = request.user,
          comment = comment,)
    
    return HttpResponseRedirect('/detail/%s'%bbs_id)


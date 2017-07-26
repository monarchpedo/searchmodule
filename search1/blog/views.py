from django.shortcuts import render
from django.shortcuts import render_to_response ,RequestContext
from blog.models import Post
from blog.forms import Postform
from blog.forms import Searchform
from django.http import HttpResponse
from django.template import Context
from BeautifulSoup import BeautifulSoup
import mechanize
from django.core.mail import send_mail
#from django.views.generic.base import templateView
# Create your views here.
# Create your views here.

def blogs(request):
       return render_to_response('blog.html',
       	               {'Posts':Post.objects.all()})

def hello(request):
       name = 'mike'
       html = "<html><body>hi %s,this semms to have worked!</body></html>" % name
       return HttpResponse(html)

def  home(request):
	   form = Postform(request.POST or None)
	   if form.is_valid():
	   	  save_it = form.save(commit=False)
	   	  save_it.save()
          
	   return  render_to_response("home.html",locals(),context_instance=RequestContext(request))
def search(request,form='Searchform'):
	#if 'q' in request.GET:
	form = Searchform(request.GET or None)
	if form.is_valid():
		text = form.cleaned_data['text']
		return render_to_response('blog.html')

	return render_to_response('search.html',locals(),context_instance=RequestContext(request))				
def thanks(request):
	return render_to_response('redbussignup.html')


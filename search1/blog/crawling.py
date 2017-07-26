import urllib3
import cgi
import cgitb
import mechanize
from BeautifulSoup import BeautifulSoup
from httpresponse import HttpResponse
from blog.models import web,Image,video
import re

#cgitb.enable()

#fo=cgi.FieldStorage()
#search = html.escape()(form["search"].value)
#if(len(search)>0):
#	print "yes\n" 
def web(term,num):
    br=mechanize.Browser() 
    br.set_handle_robots(False)
    br.addheaders = [('user-agent','chrome')]
    data="q(?!.*q).*?&amp"
    query = "https://www.google.com/search?q="+term+"&num="+num+"&filter=0"

    htmltext = br.open(query).read()

    soup = BeautifulSoup(htmltext) 
    text2=[]
    url = []
    text1= soup.findAll('div',attrs={'id':'search'})
   
	while len(text1)>0:
		   p=text1[0]
	       soup1 = BeautifulSoup(p)
           for p1 in soup1.findall('li'):
                 text2.append(p1)

           for p2  in tex2:
                soup3 = BeautifulSoup(str(p2))
                for p3 in soup3.findall('a',href="true"):
                	 #results = re.findall(patttern,str(p3))
                     url.append(p3)
            text1.pop(0)         
     print url


print web(sex,100)




def img(request):


def video(request):	
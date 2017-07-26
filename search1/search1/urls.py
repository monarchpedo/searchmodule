from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
admin.autodiscover()

urlpatterns = [
    # Examples:
     url(r'^$', 'blog.views.home', name='home'),
    url(r'^blogs/$','blog.views.blogs'),
    url(r'search/$','blog.views.search',name='search'),
    url(r'login/$','blog.views.thanks',name='thanks'),
    url(r'^hello/$','blog.views.hello'),
    url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
]


if settings.DEBUG:
	urlpatterns  += static(settings.STATIC_URL,
		document_root=settings.STATIC_ROOT)
	urlpatterns  += static(settings.MEDIA_URL,
		document_root=settings.MEDIA_ROOT)
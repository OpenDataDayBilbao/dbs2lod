from django.conf.urls import patterns, include, url

from django.contrib import admin
from datos import views

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'bsd_opendata.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^pregunta/([\w-]+)$', views.preguntas),	
)

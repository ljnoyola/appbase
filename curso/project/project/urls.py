from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^([a-z]+)/(.+)/(.+)/$', 'app1.views.calculadora', name='calculadora'),
    #url(r'^suma/(.+)/(.+)/$', 'app1.views.current_datetime', name='current_datetime'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^administrador/', include(admin.site.urls)),
)

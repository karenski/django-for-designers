from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'bookmarks.views.index', name ='home'),
    url(r'^bookmarks/$', 'bookmarks.views.index', name = 'bookmarks_view'),
    url(r'^tags/([\w-]+)/$'), 'bookmarks.views.tag'),
    url(r'^admin/', include(admin.site.urls)),
)

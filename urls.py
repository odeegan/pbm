from django.conf.urls.defaults import *
from django.contrib import admin
from django.views.generic import list_detail
from django.views.generic.simple import redirect_to

from satchmo.models import Entry
from satchmo.feeds import LatestEntriesFeed

admin.autodiscover()

object_detail_entry_dict = {
    'queryset': Entry.live.all(),
    'slug_field': 'slug',
    }

feeds = {'entries': LatestEntriesFeed}


urlpatterns = patterns('',
    (r'^$', redirect_to, {'url': '/home/'}),
    (r'^grappelli/', include('grappelli.urls')),
    (r'^admin/', include(admin.site.urls)),
    (r'^admin/filebrowser/', include('filebrowser.urls')),
    (r'^tiny_mce/', include('tinymce.urls')),
    (r'^blog/tags/', include('satchmo.urls.tags')),
    (r'^blog/', include('satchmo.urls.entries')),
    (r'^comments/', include('django.contrib.comments.urls')),
    (r'^contact/', include('contact.urls')),
    (r'^feeds/(?P<url>.*)/$',
        'django.contrib.syndication.views.feed',
        { 'feed_dict': feeds}), 
    (r'^portfolio/', include('slideshow.urls')),
    # make links to old wp site work with django version
    (r'(?P<old>^wp-content/.*)$', redirect_to, {'url': '/media/%(old)s'}),
    # make sure links to the old site still work
    # search for them in the Entry model using their slug
    (r'^\d{4}/\d{2}/(?P<slug>[-\w]+)/$',
        list_detail.object_detail,
        object_detail_entry_dict),     
)


# if we're runnning in dev, change how we serve media files
import socket
HOSTNAME = socket.gethostname()
if HOSTNAME == 'box':
    urlpatterns +=  patterns('', 
                (r'^media/(?P<path>.*)$', 
                'django.views.static.serve',
                { 'document_root': '/home/odeegan/workspace/pbm/pbm/media' }),
        )

# add our catchall URL at the end
urlpatterns +=  patterns('',
    (r'', include('custom_flatpage.urls')),
    )





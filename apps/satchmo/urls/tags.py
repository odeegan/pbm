from django.conf.urls.defaults import *
from satchmo.models import Entry
from tagging.models import Tag





urlpatterns = patterns('',
    (r'^$',
     'django.views.generic.list_detail.object_list',
     { 'queryset': Tag.objects.all() },
     'satchmo_tag_list'),
    (r'^entries/(?P<tag>[-\w]+)/$',
     'tagging.views.tagged_object_list',
     { 'queryset_or_model': Entry.live.all(),
     'template_name': 'satchmo/entries_by_tag.html' }),
     )
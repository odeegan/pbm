from django.conf.urls.defaults import *
from django.views.generic import list_detail
from django.views.generic import date_based
from django.views.generic.simple import redirect_to


from satchmo.models import Entry



list_detail_entry_dict = {
    'queryset': Entry.live.all(),
    'paginate_by': 5,                             
    }


date_based_entry_dict = {
    'queryset': Entry.live.all(),
    'date_field':'pub_date',
    }


urlpatterns = patterns('',
    (r'^$', 
     list_detail.object_list,
     list_detail_entry_dict,
     'satchmo_entry_list'),
    (r'^(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{2})/(?P<slug>[-\w]+)/$',
     date_based.object_detail,
     date_based_entry_dict,
     'satchmo_entry_detail'),)
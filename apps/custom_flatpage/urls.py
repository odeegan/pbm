from django.conf.urls.defaults import *

urlpatterns = patterns('custom_flatpage.views',
    (r'^(?P<url>.*)$', 'flatpage'),
)

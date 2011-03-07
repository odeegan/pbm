from django.template import Context, loader
from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponse
from slideshow.models import SlideShow, Image


DEFAULT_TEMPLATE = 'slideshow/default.html'



def index(request, url):
    if not url.startswith('/'):
        url = "/" + url
    
    slideshow = get_object_or_404(SlideShow, url__exact=url)

    images = slideshow.image_set.all().order_by('position')
    
    if slideshow.template_name:
        t = slideshow.template_name
    else:
        t = DEFAULT_TEMPLATE
    c = Context({
                 'slideshow': slideshow,
                 'images': images })
    return render_to_response(t, c)
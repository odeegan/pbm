from django import forms
from django.contrib import admin
from slideshow.models import SlideShow
from slideshow.models import Image


class ImageInline(admin.TabularInline):
    model = Image

class SlideShowAdmin(admin.ModelAdmin):
    url = forms.RegexField(label=("URL"), max_length=100, regex=r'^[-\w/]+$') 
    inlines = [ImageInline,]
  

class ImageAdmin(admin.ModelAdmin):
    pass

admin.site.register(SlideShow, SlideShowAdmin)

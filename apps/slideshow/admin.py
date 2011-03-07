from django import forms
from django.contrib import admin
from slideshow.models import SlideShow, Image


class ImageInline(admin.TabularInline):
    model = Image
    sortable_field_name = "position"


class SlideShowAdmin(admin.ModelAdmin):
    url = forms.RegexField(label=("URL"), max_length=100, regex=r'^[-\w/]+$') 
    inlines = [ImageInline,]

 

admin.site.register(SlideShow, SlideShowAdmin)

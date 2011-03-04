from django.contrib import admin
from django.contrib.flatpages.admin import FlatPageAdmin
from django.contrib.flatpages.models import FlatPage
from custom_flatpage.models import Image


class ImageInLine(admin.StackedInline):
    model = Image


class CustomFlatPageAdmin(FlatPageAdmin):
    inlines = [ImageInLine]

    fieldsets = (
        ('General', {
            'classes': ['extrapretty'],
            'fields': ('url', 'title')
        }),
            
    )

    
    class Media:
        js = ['/media/grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js', '/media/grappelli/tinymce_setup/tinymce_setup.js',] 


admin.site.unregister(FlatPage)
admin.site.register(FlatPage, CustomFlatPageAdmin)
from django.contrib import admin
from satchmo.models import  Entry



class EntryAdmin(admin.ModelAdmin):
    prepopulated_fields = { 'slug': ['title'] }
    class Media:
        js = ['/media/grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js', '/media/grappelli/tinymce_setup/tinymce_setup.js',] 

admin.site.register(Entry, EntryAdmin)


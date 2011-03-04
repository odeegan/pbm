from django.db import models
from django.contrib.flatpages.models import FlatPage
from filebrowser.fields import FileBrowseField



class Image(models.Model):
    url = FileBrowseField("Image", max_length=200, blank=True, null=True)
    flatpage = models.ForeignKey(FlatPage)
    alt_txt = models.CharField(max_length=100)

    def __unicode__(self):
        return self.alt_txt


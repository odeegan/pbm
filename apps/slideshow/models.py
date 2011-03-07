from django.db import models
from filebrowser.fields import FileBrowseField

class SlideShow(models.Model):
    url = models.CharField(('URL'), max_length=200, db_index=True,
        help_text = ("Example: '/about/contact/'. Make sure to have leading"
                      " and trailing slashes."))
    page_title = models.CharField(max_length=75)
    template_name = models.CharField(max_length=70, blank=True,
        help_text = ("Example: 'slideshow/seniors.html'."))

  
    class Meta:
        verbose_name_plural = "Slide Shows" 

    def __unicode__(self):
        return self.page_title
      

class Image(models.Model):
    slideshow = models.ForeignKey(SlideShow)
    #url = FileBrowseField("Image URL", max_length=200, blank=True, null=True)
    url = FileBrowseField("Image URL", max_length=200)
    position = models.PositiveSmallIntegerField("Position")
    alt_txt = models.CharField(max_length=100)
    
    class Meta:
        ordering = ['position']

    def get_thumb(self):
        return self.url.url_thumbnail

    def __unicode__(self):
        return self.alt_txt

    def get_absolute_url(self):
        return self.url


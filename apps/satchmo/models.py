import datetime

from django.contrib.auth.models import User
from django.db import models


from tagging.fields import TagField
from tagging.models import Tag


from akismet import Akismet
from django.conf import settings
from django.contrib.comments.moderation import CommentModerator, moderator
from django.utils.encoding import smart_str


class LiveEntryManager(models.Manager):
    def get_query_set(self):
        return super(LiveEntryManager, self).get_query_set().filter(
                status=self.model.LIVE_STATUS)
                   
    
       
class Entry(models.Model):
    LIVE_STATUS = 1
    DRAFT_STATUS = 2
    HIDDEN_STATUS = 3
    STATUS_CHOICES = (
        (LIVE_STATUS, 'Live'),
        (DRAFT_STATUS, 'Draft'),
        (HIDDEN_STATUS, 'Hidden'),
    )
    
    # Core fields
    title = models.CharField(max_length=250)
    body = models.TextField()
    pub_date = models.DateTimeField(default=datetime.datetime.now)
    
    # Metadata
    author = models.ForeignKey(User)
    enable_comments = models.BooleanField(default=True)    
    featured = models.BooleanField(default=False)
    slug = models.SlugField(unique_for_date='pub_date',
                            help_text="Suggested value automatically generated\
                            from title. Must be unique.")
    status = models.IntegerField(choices=STATUS_CHOICES, default=LIVE_STATUS,
                                 help_text="Only entries with live status\
                                 will be publically displayed.")

    objects = models.Manager()
    live = LiveEntryManager()


    # Tagging
    tags = TagField(help_text="Separate tags with spaces.")
    
           
    class Meta:
        ordering = ['-pub_date']
        verbose_name_plural = "Entries"
            
    def __unicode__(self):
        return self.title        
            
     
    def get_tags(self):
        return Tag.objects.get_for_object(self) 
    
    
    def get_absolute_url(self):
        return ('satchmo_entry_detail', (), {'year': self.pub_date.strftime("%Y"),
                                             'month': self.pub_date.strftime("%b").lower(),
                                             'day': self.pub_date.strftime("%d"),
                                             'slug': self.slug})
    get_absolute_url = models.permalink(get_absolute_url)


    
class EntryModerator(CommentModerator):
    auto_moderate_field = 'pub_date'
    moderate_after = 30
    email_notification = True

    def moderate_comment(self, comment, content_object, request):
        already_moderated = super(EntryModerator, self).moderate(comment, content_object)
        if already_moderated:
            return True
        akismet_api = Akismet(key=settings.AKISMET_API_KEY,
                               blog_url="http://%s/" %
                               Site.objects.get_current().domain)        
        if akismet_api.verify_key():
            akismet_data = {'comment_type': 'comment',
                             'referrer': request.META['HTTP_REFERRER'],
                             'user_ip': comment.ip_address,
                             'user_agent': request.META['HTTP_USER_AGENT']}
            return akismet_api.comment_check(smart_str(comment.comment),
                                             akismet_data,
                                             build_data=True)
        
        return False


moderator.register(Entry, EntryModerator)
    
        


  
    
        
        
        
        
        
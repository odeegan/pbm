from django.utils.feedgenerator import Atom1Feed
from django.contrib.sites.models import Site
from django.contrib.syndication.feeds import Feed
from satchmo.models import Entry

current_site = Site.objects.get_current()

class LatestEntriesFeed(Feed):
    author_name = "Monika O'Deegan"
    description = "Latest entries posted on %s" % current_site.domain
    feed_type = Atom1Feed
    item_author_name = "Monika O'Deegan"
    item_author_link = "Monika O'Deegan"
    link = "/feeds/atom/"
    title = "%s: Latest entries" % current_site.name

    def items(self):
        return Entry.live.all()[:15]
    
    def item_pubdate(self, item):
        return item.pub_date
    
    def item_guid(self, item):
        return "tag:%s,%s:%s" % (current_site.domain,
                               item.pub_date.strftime('%Y-%m-%d'),
                               item.get_absolute_url())
    
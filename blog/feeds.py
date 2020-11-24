from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords
from .models import Post

class LatestPostsFeed(Feed):
    """
    we subclass the Feed class of the syndication framework. 
    The title , link , and description attributes correspond to
    the <title> , <link> ,and <description> RSS elements, respectively.
    """
    title = 'My blog'
    link = '/blog/'
    description = 'New posts of my blog.'

    def items(self):
        # retrieves the objects to be included in the feed.
        return Post.published.all()[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        # build the description of the
        # blog post with the first 30 words.
        return truncatewords(item.body, 30)

# IMPORTANT:
"""
Django has a built-in syndication feed framework that you can use
to dynamically generate RSS or Atom feeds in a similar manner to
creating sitemaps using the site's framework. A web feed is a data
format (usually XML) that provides users with frequently updated
content.
"""
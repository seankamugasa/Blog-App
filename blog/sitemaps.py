from django.contrib.sitemaps import Sitemap
from .models import Post

class PostSitemap(Sitemap):
    """
    We create a custom sitemap by inheriting the Sitemap class of the
    sitemaps module.The changefreq and priority attributes indicate the
    change frequency of your post pages and their relevance in your
    website (the maximum value is 1). The items() method returns the
    QuerySet of objects to include in this sitemap.
    """
    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        return Post.published.all()

    def lastmod(self, obj):
        return obj.updated

"""
From settings.py

Django comes with a sitemap framework, which allows you to
generate sitemaps for your site dynamically. A sitemap is an XML
file that tells search engines the pages of your website, their
relevance, and how frequently they are updated. Using a sitemap,
you will help crawlers that index your website's content.
The Django sitemap framework depends on django.contrib.sites , which
allows you to associate objects to particular websites that are
running with your project. This comes handy when you want to run
multiple sites using a single Django project. To install the sitemap
framework, you will need to activate both the sites and the sitemap
applications in our project as shown via installed Apps.



"""
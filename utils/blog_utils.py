from django.conf import settings
from django.utils.translation import get_language
from djangocms_blog.feeds import LatestEntriesFeed
from djangocms_blog.models import Post


class CategoryFeed(LatestEntriesFeed):
    feed_items_number = settings.BLOG_FEED_CATEGORIES_ITEMS

    def get_object(self, request, category):
        return category  # pragma: no cover

    def items(self, obj=None):
        language = get_language()
        return Post.objects.filter(
            categories=obj, publish=True
        ).translated(language)[:self.feed_items_number]

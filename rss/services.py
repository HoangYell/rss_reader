import logging
import feedparser
import pytz
from time import mktime
from datetime import datetime
from rss.models import Rss
logger = logging.getLogger(__name__)


class RssService:
    """
        RssService
    """
    @classmethod
    def scrawl_service(cls, url):
        """
        scrawl data from url
        :param url: scrawl url
        :return: save scrawled data to DB
        """
        result = feedparser.parse(url)
        list_feed = result.get('entries', [])
        for feed in list_feed:
            rss = Rss()
            rss.title = feed.title if hasattr(feed, 'title') else ''
            rss.link = feed.link if hasattr(feed, 'link') else ''
            rss.description = feed.description if hasattr(feed, 'description') else ''
            rss.author = feed.author if hasattr(feed, 'author') else ''
            rss.category = feed.category if hasattr(feed, 'category') else ''
            rss.enclosure = feed.enclosure if hasattr(feed, 'enclosure') else ''
            rss.comments = feed.comments if hasattr(feed, 'comments') else ''
            rss.source = feed.source if hasattr(feed, 'source') else ''
            _published_parsed = feed.published_parsed if hasattr(feed, 'published_parsed') else ''
            _updated_parsed = feed.updated_parsed if hasattr(feed, 'updated_parsed') else ''
            pub_date = _published_parsed or _updated_parsed
            if pub_date:
                rss.pub_date = datetime.fromtimestamp(mktime(pub_date), tz=pytz.utc)
            rss.save()
        logger.info(f'{url}: scrawled {len(list_feed)} items:\n{list_feed}')

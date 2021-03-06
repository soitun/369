# Scrapy settings for crawler369 project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'crawler369'
BOT_VERSION = '1.0'

SPIDER_MODULES = ['crawler369.spiders.delfi_lt']
NEWSPIDER_MODULE = 'crawler369.spiders.new_spiders'
DEFAULT_ITEM_CLASS = 'crawler369.items.CrawlerItem'
USER_AGENT = '%s/%s' % (BOT_NAME, BOT_VERSION)
ITEM_PIPELINES = [
    'crawler369.pipelines.CommentsPipeline',
]

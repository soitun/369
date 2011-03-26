# -*- coding: utf-8 -*-
from django.db import models

SUBJECT_TYPE_ARTICLE = 1

SUBJECT_CHOICES = (
    (SUBJECT_TYPE_ARTICLE, 'Article'),
)


class BaseItem(models.Model):
    crawl_timestamp = models.DateTimeField()
    crawl_id = models.CharField(max_length=255, blank=True)
    crawl_url = models.CharField(max_length=255, blank=True)
    item_id = models.CharField(max_length=255, blank=True)
    item_link = models.CharField(max_length=500, blank=True)
    source_id = models.CharField(max_length=255, blank=True)

    class Meta:
        abstract = True


class ArticleItem(BaseItem):
    date = models.DateTimeField()
    author = models.CharField(max_length=255, blank=True)
    content = models.TextField()


class CommentItem(BaseItem):
    """
    Main class
    """
    date = models.DateTimeField()
    author = models.CharField(max_length=255, blank=True)
    content = models.TextField()
    subject_type = models.CharField(max_length=255, choices=SUBJECT_CHOICES)
    subject_id = models.CharField(max_length=255)

    def __unicode__(self):
        return u'%s (#%s), %s by %s' % (self.id, self.crawl_id, self.date, 
                                        self.author)

    class Admin:
        pass

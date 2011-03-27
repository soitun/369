# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'CommentBase'
        db.create_table('a369_commentbase', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('subject_type', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('subject_id', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('a369', ['CommentBase'])

        # Adding model 'TweetItem'
        db.create_table('a369_tweetitem', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('crawl_timestamp', self.gf('django.db.models.fields.DateTimeField')()),
            ('crawl_id', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('crawl_url', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('source_id', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('item_id', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('item_link', self.gf('django.db.models.fields.CharField')(max_length=500, blank=True)),
            ('date', self.gf('django.db.models.fields.DateTimeField')()),
            ('author', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('content', self.gf('django.db.models.fields.TextField')()),
            ('content_length', self.gf('django.db.models.fields.IntegerField')(default=0, null=True)),
            ('content_word_count', self.gf('django.db.models.fields.IntegerField')(default=0, null=True)),
            ('subject_type', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('subject_id', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('a369', ['TweetItem'])


    def backwards(self, orm):
        
        # Deleting model 'CommentBase'
        db.delete_table('a369_commentbase')

        # Deleting model 'TweetItem'
        db.delete_table('a369_tweetitem')


    models = {
        'a369.articleitem': {
            'Meta': {'object_name': 'ArticleItem'},
            'author': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'content': ('django.db.models.fields.TextField', [], {}),
            'crawl_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'crawl_timestamp': ('django.db.models.fields.DateTimeField', [], {}),
            'crawl_url': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'date': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'item_link': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            'source_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        'a369.commentbase': {
            'Meta': {'object_name': 'CommentBase'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'subject_id': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'subject_type': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'a369.commentitem': {
            'Meta': {'object_name': 'CommentItem'},
            'author': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'content': ('django.db.models.fields.TextField', [], {}),
            'content_length': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True'}),
            'content_word_count': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True'}),
            'crawl_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'crawl_timestamp': ('django.db.models.fields.DateTimeField', [], {}),
            'crawl_url': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'date': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'item_link': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            'source_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'subject_id': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'subject_type': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'a369.tweetitem': {
            'Meta': {'object_name': 'TweetItem'},
            'author': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'content': ('django.db.models.fields.TextField', [], {}),
            'content_length': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True'}),
            'content_word_count': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True'}),
            'crawl_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'crawl_timestamp': ('django.db.models.fields.DateTimeField', [], {}),
            'crawl_url': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'date': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'item_link': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            'source_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'subject_id': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'subject_type': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['a369']

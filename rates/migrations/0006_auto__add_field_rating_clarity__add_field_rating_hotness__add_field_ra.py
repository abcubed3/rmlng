# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Rating.clarity'
        db.add_column(u'rates_rating', 'clarity',
                      self.gf('django.db.models.fields.CharField')(default=1, max_length=1),
                      keep_default=False)

        # Adding field 'Rating.hotness'
        db.add_column(u'rates_rating', 'hotness',
                      self.gf('django.db.models.fields.CharField')(default=1, max_length=1),
                      keep_default=False)

        # Adding field 'Rating.handout'
        db.add_column(u'rates_rating', 'handout',
                      self.gf('django.db.models.fields.CharField')(default=1, max_length=1),
                      keep_default=False)

        # Adding field 'Rating.course'
        db.add_column(u'rates_rating', 'course',
                      self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Rating.recommend'
        db.add_column(u'rates_rating', 'recommend',
                      self.gf('django.db.models.fields.CharField')(default=1, max_length=1),
                      keep_default=False)

        # Adding field 'Rating.describe'
        db.add_column(u'rates_rating', 'describe',
                      self.gf('django.db.models.fields.TextField')(default='Enter just 160 character description of your lecturer', max_length=160),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Rating.clarity'
        db.delete_column(u'rates_rating', 'clarity')

        # Deleting field 'Rating.hotness'
        db.delete_column(u'rates_rating', 'hotness')

        # Deleting field 'Rating.handout'
        db.delete_column(u'rates_rating', 'handout')

        # Deleting field 'Rating.course'
        db.delete_column(u'rates_rating', 'course')

        # Deleting field 'Rating.recommend'
        db.delete_column(u'rates_rating', 'recommend')

        # Deleting field 'Rating.describe'
        db.delete_column(u'rates_rating', 'describe')


    models = {
        u'institutions.institution': {
            'Meta': {'object_name': 'Institution'},
            'abr': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'colors': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'established': ('django.db.models.fields.DateField', [], {}),
            'former': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'formerName': ('django.db.models.fields.CharField', [], {'max_length': '120', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'motto': ('django.db.models.fields.CharField', [], {'max_length': '120', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'nickName': ('django.db.models.fields.CharField', [], {'max_length': '120', 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'}),
            'students': ('django.db.models.fields.IntegerField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'updated_Timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'vc': ('django.db.models.fields.CharField', [], {'max_length': '120', 'null': 'True', 'blank': 'True'}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        u'lecturers.lecturer': {
            'Meta': {'object_name': 'Lecturer'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'currentPosition': ('django.db.models.fields.CharField', [], {'max_length': '120', 'null': 'True', 'blank': 'True'}),
            'department': ('django.db.models.fields.CharField', [], {'max_length': '120', 'null': 'True', 'blank': 'True'}),
            'firstName': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lastName': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'middleName': ('django.db.models.fields.CharField', [], {'max_length': '120', 'null': 'True', 'blank': 'True'}),
            'rate': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'max_digits': '3', 'decimal_places': '2'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '12', 'null': 'True', 'blank': 'True'}),
            'university': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['institutions.Institution']"}),
            'updated_Timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'rates.rating': {
            'Meta': {'object_name': 'Rating'},
            'clarity': ('django.db.models.fields.CharField', [], {'default': '1', 'max_length': '1'}),
            'course': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'describe': ('django.db.models.fields.TextField', [], {'default': "'Enter just 160 character description of your lecturer'", 'max_length': '160'}),
            'handout': ('django.db.models.fields.CharField', [], {'default': '1', 'max_length': '1'}),
            'helpfulness': ('django.db.models.fields.CharField', [], {'default': '1', 'max_length': '1'}),
            'hotness': ('django.db.models.fields.CharField', [], {'default': '1', 'max_length': '1'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'knowlegdeable': ('django.db.models.fields.CharField', [], {'default': '1', 'max_length': '1'}),
            'lecturer': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['lecturers.Lecturer']"}),
            'rating': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'max_digits': '3', 'decimal_places': '2'}),
            'rating_time': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'recommend': ('django.db.models.fields.CharField', [], {'default': '1', 'max_length': '1'})
        }
    }

    complete_apps = ['rates']
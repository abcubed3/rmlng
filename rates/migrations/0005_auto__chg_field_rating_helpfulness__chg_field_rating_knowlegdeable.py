# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Rating.helpfulness'
        db.alter_column(u'rates_rating', 'helpfulness', self.gf('django.db.models.fields.CharField')(max_length=1))

        # Changing field 'Rating.knowlegdeable'
        db.alter_column(u'rates_rating', 'knowlegdeable', self.gf('django.db.models.fields.CharField')(max_length=1))

    def backwards(self, orm):

        # Changing field 'Rating.helpfulness'
        db.alter_column(u'rates_rating', 'helpfulness', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'Rating.knowlegdeable'
        db.alter_column(u'rates_rating', 'knowlegdeable', self.gf('django.db.models.fields.CharField')(max_length=50))

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
            'helpfulness': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'knowlegdeable': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'lecturer': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['lecturers.Lecturer']"}),
            'rating': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'max_digits': '3', 'decimal_places': '2'}),
            'rating_time': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['rates']
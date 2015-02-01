# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Rating'
        db.create_table(u'rates_rating', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('rating', self.gf('django.db.models.fields.DecimalField')(default=0.0, max_digits=3, decimal_places=2)),
            ('rating_time', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'rates', ['Rating'])

        # Deleting field 'Rate.updated_Timestamp'
        db.delete_column(u'rates_rate', 'updated_Timestamp')


    def backwards(self, orm):
        # Deleting model 'Rating'
        db.delete_table(u'rates_rating')

        # Adding field 'Rate.updated_Timestamp'
        db.add_column(u'rates_rate', 'updated_Timestamp',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now=True, default=datetime.datetime(2015, 1, 31, 0, 0), blank=True),
                      keep_default=False)


    models = {
        u'rates.rate': {
            'Meta': {'object_name': 'Rate'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'rates': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'max_digits': '3', 'decimal_places': '2'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
        },
        u'rates.rating': {
            'Meta': {'object_name': 'Rating'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'rating': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'max_digits': '3', 'decimal_places': '2'}),
            'rating_time': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['rates']
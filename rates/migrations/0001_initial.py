# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Rate'
        db.create_table(u'rates_rate', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('rates', self.gf('django.db.models.fields.DecimalField')(default=0.0, max_digits=3, decimal_places=2)),
            ('timestamp', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated_Timestamp', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'rates', ['Rate'])


    def backwards(self, orm):
        # Deleting model 'Rate'
        db.delete_table(u'rates_rate')


    models = {
        u'rates.rate': {
            'Meta': {'object_name': 'Rate'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'rates': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'max_digits': '3', 'decimal_places': '2'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'updated_Timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['rates']
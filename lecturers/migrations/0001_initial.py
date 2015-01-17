# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Lecturer'
        db.create_table(u'lecturers_lecturer', (
            ('l_ID', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=60, null=True, blank=True)),
            ('firstName', self.gf('django.db.models.fields.CharField')(max_length=120)),
            ('middleName', self.gf('django.db.models.fields.CharField')(max_length=120, null=True, blank=True)),
            ('lastName', self.gf('django.db.models.fields.CharField')(max_length=120)),
            ('currentPosition', self.gf('django.db.models.fields.CharField')(max_length=120, null=True, blank=True)),
            ('timestamp', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated_Timestamp', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'lecturers', ['Lecturer'])


    def backwards(self, orm):
        # Deleting model 'Lecturer'
        db.delete_table(u'lecturers_lecturer')


    models = {
        u'lecturers.lecturer': {
            'Meta': {'object_name': 'Lecturer'},
            'currentPosition': ('django.db.models.fields.CharField', [], {'max_length': '120', 'null': 'True', 'blank': 'True'}),
            'firstName': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'l_ID': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'lastName': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'middleName': ('django.db.models.fields.CharField', [], {'max_length': '120', 'null': 'True', 'blank': 'True'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '60', 'null': 'True', 'blank': 'True'}),
            'updated_Timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['lecturers']
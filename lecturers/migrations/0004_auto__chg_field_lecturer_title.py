# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Lecturer.title'
        db.alter_column(u'lecturers_lecturer', 'title', self.gf('django.db.models.fields.CharField')(max_length=12, null=True))

    def backwards(self, orm):

        # Changing field 'Lecturer.title'
        db.alter_column(u'lecturers_lecturer', 'title', self.gf('django.db.models.fields.CharField')(max_length=60, null=True))

    models = {
        u'lecturers.lecturer': {
            'Meta': {'object_name': 'Lecturer'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'currentPosition': ('django.db.models.fields.CharField', [], {'max_length': '120', 'null': 'True', 'blank': 'True'}),
            'department': ('django.db.models.fields.CharField', [], {'max_length': '120', 'null': 'True', 'blank': 'True'}),
            'firstName': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'lastName': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'middleName': ('django.db.models.fields.CharField', [], {'max_length': '120', 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '12', 'null': 'True', 'blank': 'True'}),
            'updated_Timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['lecturers']
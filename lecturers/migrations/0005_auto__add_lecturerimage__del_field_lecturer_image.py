# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'LecturerImage'
        db.create_table(u'lecturers_lecturerimage', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('lecturer', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['lecturers.Lecturer'])),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True)),
            ('featured', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('timestamp', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated_Timestamp', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'lecturers', ['LecturerImage'])

        # Deleting field 'Lecturer.image'
        db.delete_column(u'lecturers_lecturer', 'image')


    def backwards(self, orm):
        # Deleting model 'LecturerImage'
        db.delete_table(u'lecturers_lecturerimage')

        # Adding field 'Lecturer.image'
        db.add_column(u'lecturers_lecturer', 'image',
                      self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True),
                      keep_default=False)


    models = {
        u'lecturers.lecturer': {
            'Meta': {'object_name': 'Lecturer'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'currentPosition': ('django.db.models.fields.CharField', [], {'max_length': '120', 'null': 'True', 'blank': 'True'}),
            'department': ('django.db.models.fields.CharField', [], {'max_length': '120', 'null': 'True', 'blank': 'True'}),
            'firstName': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lastName': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'middleName': ('django.db.models.fields.CharField', [], {'max_length': '120', 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '12', 'null': 'True', 'blank': 'True'}),
            'updated_Timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'lecturers.lecturerimage': {
            'Meta': {'object_name': 'LecturerImage'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'featured': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True'}),
            'lecturer': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['lecturers.Lecturer']"}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'updated_Timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['lecturers']
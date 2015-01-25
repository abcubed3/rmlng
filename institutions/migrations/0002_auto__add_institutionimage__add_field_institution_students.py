# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'InstitutionImage'
        db.create_table(u'institutions_institutionimage', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('institution', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['institutions.Institution'])),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True)),
            ('featured', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('timestamp', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated_Timestamp', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'institutions', ['InstitutionImage'])

        # Adding field 'Institution.students'
        db.add_column(u'institutions_institution', 'students',
                      self.gf('django.db.models.fields.IntegerField')(max_length=10, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'InstitutionImage'
        db.delete_table(u'institutions_institutionimage')

        # Deleting field 'Institution.students'
        db.delete_column(u'institutions_institution', 'students')


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
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'students': ('django.db.models.fields.IntegerField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'updated_Timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'vc': ('django.db.models.fields.CharField', [], {'max_length': '120', 'null': 'True', 'blank': 'True'}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        u'institutions.institutionimage': {
            'Meta': {'object_name': 'InstitutionImage'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'featured': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True'}),
            'institution': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['institutions.Institution']"}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'updated_Timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['institutions']
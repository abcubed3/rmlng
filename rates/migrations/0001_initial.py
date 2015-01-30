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
            ('currentRate', self.gf('django.db.models.fields.IntegerField')(default=0.0, max_length=3)),
            ('timestamp', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated_Timestamp', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'rates', ['Rate'])

        # Adding M2M table for field lecturer on 'Rate'
        m2m_table_name = db.shorten_name(u'rates_rate_lecturer')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('rate', models.ForeignKey(orm[u'rates.rate'], null=False)),
            ('lecturer', models.ForeignKey(orm[u'lecturers.lecturer'], null=False))
        ))
        db.create_unique(m2m_table_name, ['rate_id', 'lecturer_id'])

        # Adding model 'Rating'
        db.create_table(u'rates_rating', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('lecturer', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['lecturers.Lecturer'])),
            ('rate', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['rates.Rate'])),
            ('rating', self.gf('django.db.models.fields.IntegerField')(default=0.0)),
            ('timestamp', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'rates', ['Rating'])


    def backwards(self, orm):
        # Deleting model 'Rate'
        db.delete_table(u'rates_rate')

        # Removing M2M table for field lecturer on 'Rate'
        db.delete_table(db.shorten_name(u'rates_rate_lecturer'))

        # Deleting model 'Rating'
        db.delete_table(u'rates_rating')


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
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '12', 'null': 'True', 'blank': 'True'}),
            'updated_Timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'rates.rate': {
            'Meta': {'object_name': 'Rate'},
            'currentRate': ('django.db.models.fields.IntegerField', [], {'default': '0.0', 'max_length': '3'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lecturer': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['lecturers.Lecturer']", 'symmetrical': 'False'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'updated_Timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'rates.rating': {
            'Meta': {'object_name': 'Rating'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lecturer': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['lecturers.Lecturer']"}),
            'rate': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['rates.Rate']"}),
            'rating': ('django.db.models.fields.IntegerField', [], {'default': '0.0'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['rates']
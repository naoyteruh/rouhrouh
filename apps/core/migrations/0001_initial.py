# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Quotation'
        db.create_table(u'core_quotation', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('text', self.gf('django.db.models.fields.TextField')()),
            ('author', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'core', ['Quotation'])

        # Adding model 'Prestation'
        db.create_table(u'core_prestation', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('offers', self.gf('django.db.models.fields.CharField')(default='', max_length=30, blank=True)),
            ('data', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('price', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('fidelity', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('comments', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'core', ['Prestation'])


    def backwards(self, orm):
        # Deleting model 'Quotation'
        db.delete_table(u'core_quotation')

        # Deleting model 'Prestation'
        db.delete_table(u'core_prestation')


    models = {
        u'core.prestation': {
            'Meta': {'object_name': 'Prestation'},
            'comments': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'data': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'fidelity': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'offers': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '30', 'blank': 'True'}),
            'price': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'core.quotation': {
            'Meta': {'object_name': 'Quotation'},
            'author': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {})
        }
    }

    complete_apps = ['core']
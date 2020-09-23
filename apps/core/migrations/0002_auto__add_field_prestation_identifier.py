# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Prestation.identifier'
        db.add_column(u'core_prestation', 'identifier',
                      self.gf('django.db.models.fields.CharField')(default='toto', max_length=30),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Prestation.identifier'
        db.delete_column(u'core_prestation', 'identifier')


    models = {
        u'core.prestation': {
            'Meta': {'object_name': 'Prestation'},
            'comments': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'data': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'fidelity': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'identifier': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
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
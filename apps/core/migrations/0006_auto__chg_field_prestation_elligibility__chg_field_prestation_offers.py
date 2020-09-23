# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Prestation.elligibility'
        db.alter_column(u'core_prestation', 'elligibility', self.gf('django.db.models.fields.CharField')(max_length=200))

        # Changing field 'Prestation.offers'
        db.alter_column(u'core_prestation', 'offers', self.gf('django.db.models.fields.CharField')(max_length=200))

    def backwards(self, orm):

        # Changing field 'Prestation.elligibility'
        db.alter_column(u'core_prestation', 'elligibility', self.gf('django.db.models.fields.CharField')(max_length=30))

        # Changing field 'Prestation.offers'
        db.alter_column(u'core_prestation', 'offers', self.gf('django.db.models.fields.CharField')(max_length=30))

    models = {
        u'core.prestation': {
            'Meta': {'object_name': 'Prestation'},
            'comments': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'data': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'data_offers': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '30', 'blank': 'True'}),
            'elligibility': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'blank': 'True'}),
            'fidelity': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'identifier': ('django.db.models.fields.CharField', [], {'max_length': '36'}),
            'offers': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'blank': 'True'}),
            'price': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'provider': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '30', 'blank': 'True'})
        },
        u'core.quotation': {
            'Meta': {'object_name': 'Quotation'},
            'author': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {})
        }
    }

    complete_apps = ['core']
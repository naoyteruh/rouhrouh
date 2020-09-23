# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Prestation.commitment'
        db.delete_column(u'core_prestation', 'commitment')

        # Deleting field 'Prestation.subscription'
        db.delete_column(u'core_prestation', 'subscription')


    def backwards(self, orm):
        # Adding field 'Prestation.commitment'
        db.add_column(u'core_prestation', 'commitment',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Prestation.subscription'
        db.add_column(u'core_prestation', 'subscription',
                      self.gf('django.db.models.fields.DateField')(default='', blank=True),
                      keep_default=False)


    models = {
        u'core.prestation': {
            'Meta': {'object_name': 'Prestation'},
            'comment': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'blank': 'True'}),
            'data': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'data_offers': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '30', 'blank': 'True'}),
            'elligibility': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'blank': 'True'}),
            'email': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'blank': 'True'}),
            'fidelity': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'identifier': ('django.db.models.fields.CharField', [], {'max_length': '36'}),
            'is_blocked': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_confirmed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_guest': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_mms_unlimited': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_phone_credit': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_sms_unlimited': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
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
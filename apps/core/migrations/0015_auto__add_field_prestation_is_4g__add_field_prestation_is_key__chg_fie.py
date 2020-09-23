# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Prestation.is_4g'
        db.add_column(u'core_prestation', 'is_4g',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Prestation.is_key'
        db.add_column(u'core_prestation', 'is_key',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


        # Changing field 'Prestation.subscription'
        db.alter_column(u'core_prestation', 'subscription', self.gf('django.db.models.fields.DateField')(null=True))

    def backwards(self, orm):
        # Deleting field 'Prestation.is_4g'
        db.delete_column(u'core_prestation', 'is_4g')

        # Deleting field 'Prestation.is_key'
        db.delete_column(u'core_prestation', 'is_key')


        # Changing field 'Prestation.subscription'
        db.alter_column(u'core_prestation', 'subscription', self.gf('django.db.models.fields.DateField')())

    models = {
        u'core.prestation': {
            'Meta': {'object_name': 'Prestation'},
            'comment': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'blank': 'True'}),
            'commitment': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'data': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'data_offers': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '30', 'blank': 'True'}),
            'elligibility': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'blank': 'True'}),
            'email': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'blank': 'True'}),
            'fidelity': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'identifier': ('django.db.models.fields.CharField', [], {'max_length': '36'}),
            'is_4g': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_blocked': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_confirmed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_guest': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_key': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_mms_unlimited': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_phone_credit': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_sms_unlimited': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'offers': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'blank': 'True'}),
            'price': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'provider': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '30', 'blank': 'True'}),
            'subscription': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2016, 1, 21, 0, 0)', 'null': 'True', 'blank': 'True'})
        },
        u'core.quotation': {
            'Meta': {'object_name': 'Quotation'},
            'author': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {})
        }
    }

    complete_apps = ['core']
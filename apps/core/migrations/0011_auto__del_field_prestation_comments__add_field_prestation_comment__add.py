# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Prestation.comments'
        db.delete_column(u'core_prestation', 'comments')

        # Adding field 'Prestation.comment'
        db.add_column(u'core_prestation', 'comment',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=200, blank=True),
                      keep_default=False)

        # Adding field 'Prestation.is_sms_unlimited'
        db.add_column(u'core_prestation', 'is_sms_unlimited',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Prestation.is_mms_unlimited'
        db.add_column(u'core_prestation', 'is_mms_unlimited',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Prestation.is_blocked'
        db.add_column(u'core_prestation', 'is_blocked',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Prestation.is_phone_credit'
        db.add_column(u'core_prestation', 'is_phone_credit',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Prestation.comments'
        db.add_column(u'core_prestation', 'comments',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=200),
                      keep_default=False)

        # Deleting field 'Prestation.comment'
        db.delete_column(u'core_prestation', 'comment')

        # Deleting field 'Prestation.is_sms_unlimited'
        db.delete_column(u'core_prestation', 'is_sms_unlimited')

        # Deleting field 'Prestation.is_mms_unlimited'
        db.delete_column(u'core_prestation', 'is_mms_unlimited')

        # Deleting field 'Prestation.is_blocked'
        db.delete_column(u'core_prestation', 'is_blocked')

        # Deleting field 'Prestation.is_phone_credit'
        db.delete_column(u'core_prestation', 'is_phone_credit')


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
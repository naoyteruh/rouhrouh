# -*- coding: utf8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _
from datetime import datetime


class AjaxReturn():
    def __init__(self, status, data, message=""):
        self.status = status
        self.data = data
        self.message = message


class Quotation(models.Model):
    text = models.TextField()
    author = models.CharField(max_length=200)

    def __unicode__(self):
        return u'%s' % (self.author)


OFFRES = (
    ("mobile", "forfait mobile seul"),
    ("fixe", "forfait fixe seul"),
    ("triplay", "forfait internet + fixe + TV"),
    ("quadriplay", "forfait internet + fixe + mobile + TV"),
)

OPERATEURS = (
    ("orange", "Orange"),
    ("sfr", "Sfr"),
    ("bouygues", "Bouygues Telecom"),
    ("free", "Free"),
    ("autre", "Autre")
)

OFFRES_DATAS = (
    ("m200mo", "Moins de 200Mo"),    
    ("200mo", "de 200Mo à 1Go"),
    ("1go", "1Go"),
    ("3go", "3Go"),
    ("6go", "6Go"),
    ("8go", "8Go"),
    ("10go", "10Go"),
    ("50go", "50Go"),
    ("autre", "Autre")
)

NONE=0
LOW=6
MEDIUM=12
HIGH=24
ENGAGEMENTS = (
    (NONE, "Aucun"),
    (LOW, "6 mois"),
    (MEDIUM, "12 mois"),
    (HIGH, "24 mois")
)


def get_offers():
    return OFFRES

def get_providers():
    return OPERATEURS

def get_data_offers():
    return OFFRES_DATAS

def get_commitments():
    return ENGAGEMENTS

class Prestation(models.Model):
    provider = models.CharField(_('opérateur'), max_length=30, choices=OPERATEURS, default="", blank=True)
    elligibility = models.CharField(_('elligibilité'), max_length=200, default="", blank=True)
    identifier = models.CharField(_('identifiant'), max_length=36)
    offers = models.CharField(_('offres'), max_length=200, choices=OFFRES, default="", blank=True)
    data_offers = models.CharField(_('offres datas'), max_length=30, choices=OFFRES_DATAS, default="", blank=True)
    data = models.IntegerField(default=0)
    price = models.IntegerField(default=0)
    fidelity = models.BooleanField()
    comment = models.CharField(max_length=200, default="", blank=True)
    email = models.CharField(_('email'), max_length=200, default="", blank=True)
    is_guest = models.BooleanField()
    is_confirmed = models.BooleanField()
    is_sms_unlimited = models.BooleanField()
    is_mms_unlimited = models.BooleanField()
    is_blocked = models.BooleanField()
    is_phone_credit = models.BooleanField()
    is_4g = models.BooleanField()
    is_key = models.BooleanField()
    commitment = models.IntegerField(default=0, choices=ENGAGEMENTS)
    subscription = models.DateField(default=datetime.now(), null=True, blank=True)
    class Meta:
        verbose_name = "Prestation"
        verbose_name_plural = "Prestations"

    def __str__(self):
        return u'%s - %s - %s (%s)' % (self.provider, self.offers, self.price, self.email)

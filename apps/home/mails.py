# -*- coding: utf-8 -*-
from django.core.mail import EmailMultiAlternatives
from django.core.urlresolvers import reverse
from home.templatetags.currency_tags import *
from core.models import *

DICTIONARIES = {
    "offers": dict(get_offers()),
    "providers": dict(get_providers()),
    "data_offers": dict(get_data_offers()),
    "commitments": dict(get_commitments()),
}

def humabool(boolean):
    if boolean:
        return "Oui"
    else:
        return "Non"

def get_prestation_resume(prestation):
    isMobile = prestation.offers == 'mobile' or prestation.offers == 'quadriplay'
    result = "<p> R&eacute;sum&eacute;: </p>"
    result += "<ul>"
    result += "<li>Op&eacute;rateur: %s</li>" % DICTIONARIES["providers"][prestation.provider]
    result += "<li>Offre: %s</li>" % DICTIONARIES["offers"][prestation.offers]
    if isMobile:
        result += "<li>SMS illimit&eacute;s: %s</li>" % humabool(prestation.is_sms_unlimited)
        result += "<li>MMS illimit&eacute;s: %s</li>" % humabool(prestation.is_mms_unlimited)
        result += "<li>Acc&egrave;s 4G: %s</li>" % humabool(prestation.is_4g)
        result += "<li>Acc&egrave;s ordinateur: %s</li>" % humabool(prestation.is_key)
        result += "<li>Forfait bloqu&eacute;: %s</li>" % humabool(prestation.is_blocked)
        result += "<li>Remboursement t&eacute;l&eacute;phone: %s</li>" % humabool(prestation.is_phone_credit)
        if prestation.data_offers != 'autre':
            result += "<li>Donn&eacute;es: %s</li>" % DICTIONARIES["data_offers"][prestation.data_offers]
        else:
            result += "<li>Donn&eacute;es: %s</li>" % prestation.data
        result += "<li>Engagement: %s</li>" % DICTIONARIES["commitments"][prestation.commitment]
        if prestation.commitment and prestation.subscription:
            result += "<li>Date de souscription: %s</li>" % prestation.subscription
    result += "<li>Avantages fidelit&eacute;: %s</li>" % humabool(prestation.fidelity)
    result += "<li>Prix pay&eacute;: %s&euro;</li>" % format_currency(prestation.price, 2, ",")
    result += "<li>Mode invit&eacute;: %s</li>" % humabool(prestation.is_guest)
    result += "</ul>"
    return result

def send_add_mail(request, prestation):
    to_email = prestation.email
    subject, from_email = 'rouhRouh - Prestation ajoutée !', 'ne_pas_repondre@ekilibr-informatique.net'
    text_content = 'Votre prestation a &eacute;t&eacute; ajout&eacute;e sur rouhRouh !'
    html_content = '<p>Votre prestation a &eacute;t&eacute; ajout&eacute;e sur <strong>rouhRouh</strong> !</p>'
    html_content += '<p>Pour la confirmer, cliquez '
    html_content += '<a href="'
    html_content += 'http://'
    html_content += request.environ['HTTP_HOST']
    html_content += reverse("confirm", args=[prestation.identifier])
    html_content += '">ici</a>.</p>'
    html_content += get_prestation_resume(prestation)
    html_content += '<p>Merci pour votre participation.</p>'
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to_email])
    msg.attach_alternative(html_content, "text/html")
    msg.send(fail_silently=False)

def send_confim_mail(request, prestation):
    to_email = prestation.email
    subject, from_email = 'rouhRouh - Prestation confirmée !', 'ne_pas_repondre@ekilibr-informatique.net'
    text_content = 'Votre prestation a &eacute;t&eacute; confirm&eacute;e sur rouhRouh !'
    html_content = '<p>Votre prestation a &eacute;t&eacute; confirm&eacute;e sur <strong>rouhRouh</strong> !</p>'
    html_content += '<p>Si vous souhaitez visualiser votre classement, cliquez '
    html_content += '<a href="'
    html_content += 'http://'
    html_content += request.environ['HTTP_HOST']
    html_content += reverse("consult", args=[prestation.identifier])
    html_content += '">ici</a>.</p>'
    html_content += '<p>Si vous souhaitez modifier votre prestation, cliquez '
    html_content += '<a href="'
    html_content += 'http://'
    html_content += request.environ['HTTP_HOST']
    html_content += reverse("edit", args=[prestation.identifier])
    html_content += '">ici</a>.</p>'
    html_content += '<p>Pour vous d&eacute;sabonner et supprimer votre prestation, cliquez '
    html_content += '<a href="'
    html_content += 'http://'
    html_content += request.environ['HTTP_HOST']
    html_content += reverse("unsubscribe", args=[prestation.identifier])
    html_content += '">ici</a>.</p>'
    html_content += get_prestation_resume(prestation)
    html_content += '<p>Merci pour votre participation.</p>'
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to_email])
    msg.attach_alternative(html_content, "text/html")
    msg.send(fail_silently=False)
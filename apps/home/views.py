# -*- coding: utf-8 -*-
import sys, os
from django.shortcuts import redirect, render_to_response, HttpResponse
from django.core.urlresolvers import reverse
from django.template import RequestContext
from core.models import *
import json
from django.core import serializers
from django.forms.models import model_to_dict
from django.db.models import Avg, Max, Min
import uuid
from django.core.urlresolvers import resolve
import logging
from mails import *
from datetime import *

logger = logging.getLogger(__name__)

DEFAULT_PARAMETERS = {
    "offers": get_offers(),
    "providers": get_providers(),
    "data_offers": get_data_offers(),
    "commitments": get_commitments(),
}

class DatetimeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, (datetime,)):
            return obj.strftime('%Y-%m-%dT%H:%M:%SZ')
        elif isinstance(obj, (date,)):
            return obj.strftime('%Y-%m-%d')
        # Let the base class default method raise the TypeError
        return json.JSONEncoder.default(self, obj)

def set_view_parameters(extra_parameters = {}, state = "HOME", server_error=None, redirection=None):
    parameters = DEFAULT_PARAMETERS.copy()
    parameters.update(extra_parameters)
    parameters['state'] = state
    parameters['server_error'] = server_error
    parameters['redirection'] = redirection
    return parameters

def homepage(request):

    if request.is_ajax() or request.method == 'POST':
        try:
            # Parsing requete
            json_data = json.loads(request.body)

            if 'identifier' not in json_data or json_data['identifier'] == '':
                mode = "CREATION"
            else:
                mode = "EDITION"

            # Stockage en base
            if mode == "CREATION":
                prestation = Prestation()
                prestation.identifier = str(uuid.uuid4())
            if mode == "EDITION":
                prestation = Prestation.objects.get(identifier=json_data['identifier'])

            prestation.provider = json_data['provider']
            prestation.offers = json_data['offer']
            if prestation.offers == 'mobile':
                elligibility = [t[0] for t in get_providers()]
            else:
                elligibility = json_data['elligibility']
            if prestation.provider not in elligibility:
                elligibility.append(prestation.provider)
            prestation.elligibility = "|".join(elligibility)
            if prestation.offers == 'mobile' or prestation.offers == 'quadriplay':
            	prestation.data_offers = json_data['data_offer']
            	if prestation.data_offers == 'autre':
            		prestation.data = json_data['data']
            prestation.price = int(round(float(json_data['price'])*100))
            prestation.fidelity = json_data['fidelity']
            prestation.is_guest = json_data['is_guest']
            if 'email' in json_data:
                prestation.email = json_data['email']

            prestation.comment = json_data['comment']
            prestation.is_sms_unlimited = json_data['is_sms_unlimited']
            prestation.is_mms_unlimited = json_data['is_mms_unlimited']
            prestation.is_4g = json_data['is_4g']
            prestation.is_key = json_data['is_key']
            prestation.is_blocked = json_data['is_blocked']
            prestation.is_phone_credit = json_data['is_phone_credit']
            if 'commitment' in json_data and json_data['commitment']:
                prestation.commitment = json_data['commitment']
            if 'subscription' in json_data and json_data['subscription']:
                prestation.subscription = json_data['subscription']

            prestation.save()

            # Recuperation de l'objet stocké
            prestation = Prestation.objects.get(identifier=prestation.identifier)

            # Envoi email
            if 'email' in json_data:
                # Envoi email
                send_add_mail(request, prestation)

            ajaxReturn = AjaxReturn("OK", model_to_dict(prestation))
        except Exception as e:
            logger.error('Une erreur est survenue : %s' % e.message)
            ajaxReturn = AjaxReturn("KO", {}, e.message)
        return HttpResponse(json.dumps(ajaxReturn.__dict__, cls=DatetimeEncoder), mimetype="application/json")

    # Mode ajout d une prestation
    return render_to_response("homepage.html", set_view_parameters(state="CREATION"), RequestContext(request))

def consult(request, identifier):
    try:
        # Recuperation prestation
        server_error = ""
        prestation = Prestation.objects.get(identifier=identifier)
        if prestation:
            if not prestation.is_confirmed:
                server_error = "Prestation non confirmée"
                return render_to_response("homepage.html", \
                        set_view_parameters(state="CONSULTATION", server_error=server_error), \
                        RequestContext(request))
            else:
                # Recuperation donnees
                prestations = get_stats_datas(prestation.identifier)
                prestations_json = json.dumps(prestations, cls=DatetimeEncoder)
                # Redirection
                return render_to_response("homepage.html", \
                        set_view_parameters({"prestation_json": json.dumps(model_to_dict(prestation), cls=DatetimeEncoder), "prestations_json": prestations_json}, \
                                            state="CONSULTATION", server_error=server_error), \
                        RequestContext(request))
                #return redirect(reverse("consult", args=[prestation.identifier]))
    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print(exc_type, fname, exc_tb.tb_lineno)
        #print e.message
        logger.error('Une erreur est survenue : %s' % e.message)
        pass

    return redirect('homepage')

def confirm(request, identifier):
    try:
        # Recuperation prestation
        server_error = ""
        prestation = Prestation.objects.get(identifier=identifier)
        if prestation:
            if not prestation.is_confirmed:
                # MAJ prestation
                prestation.is_confirmed = True
                prestation.save()
                # Envoi email
                send_confim_mail(request, prestation)
                # MAJ prestation
                if prestation.is_guest:
                    prestation.email = ""
                    prestation.save()
                # Recuperation donnees
                prestations = get_stats_datas(prestation.identifier)
                prestations_json = json.dumps(prestations, cls=DatetimeEncoder)
                # Redirection
                return render_to_response("homepage.html", \
                    set_view_parameters({"prestation_json": json.dumps(model_to_dict(prestation), cls=DatetimeEncoder), "prestations_json": prestations_json}, \
                                        state="CONFIRMATION"), \
                    RequestContext(request))
            else:
                server_error = "Prestation déjà confirmée"
                redirection = reverse("consult", args=[prestation.identifier])
                # Recuperation donnees
                prestations = get_stats_datas(prestation.identifier)
                prestations_json = json.dumps(prestations, cls=DatetimeEncoder)
                # Redirection
                return redirect(reverse("consult", args=[prestation.identifier]))
    except Exception as e:
        logger.error('Une erreur est survenue : %s' % e.message)
        pass
    return redirect('homepage')

def edit(request, identifier):
    try:
        prestation = Prestation.objects.get(identifier=identifier)
        if prestation:
            # Prestation non confirmee
            if prestation.is_confirmed:
                return render_to_response("homepage.html", \
                    set_view_parameters({"prestation": prestation}, state="EDITION"), \
                    RequestContext(request))
            else:
                server_error = "Prestation non confirmée"
                return render_to_response("homepage.html", \
                        set_view_parameters(server_error=server_error), \
                        RequestContext(request))
    except Exception as e:
        logger.error('Une erreur est survenue : %s' % e.message)
        pass
    return redirect('homepage')

def unsubscribe(request, identifier):
    try:
        prestation = Prestation.objects.get(identifier=identifier)
        if prestation:
            prestation.delete()
            return render_to_response("homepage.html", \
                    set_view_parameters(state="UNSUBSCRIPTION"), \
                    RequestContext(request))
    except Exception as e:
        logger.error('Une erreur est survenue : %s' % e.message)
        pass
    return redirect('homepage')


############
#   METHODES UTILITAIRES
############
def get_stats_datas(identifier):

    prestations = list()
    included_keys = ['data', 'offers', 'price', 'provider', 'is_phone_credit', \
         'is_sms_unlimited', 'is_mms_unlimited', 'is_blocked', 'is_4g', 'is_key', \
         'fidelity', 'data_offers', 'data']

    # Recuperation de la prestation courante
    prestation = Prestation.objects.get(identifier = identifier)

    # Filtrage des retours plus interessants
    better_prestations = Prestation.objects.annotate(Min('price')).order_by('price').filter(offers=prestation.offers, \
                                            price__lt=prestation.price, \
                                            provider__in=prestation.elligibility.split('|'))
    if prestation.is_sms_unlimited:
        better_prestations = better_prestations.filter(is_sms_unlimited=True)
    if prestation.is_mms_unlimited:
        better_prestations = better_prestations.filter(is_mms_unlimited=True)
    if prestation.is_phone_credit:
        better_prestations = better_prestations.filter(is_phone_credit=True)
    if not prestation.is_blocked:
        better_prestations = better_prestations.filter(is_blocked=False)
    if prestation.is_4g:
        better_prestations = better_prestations.filter(is_4g=True)
    if prestation.is_key:
        better_prestations = better_prestations.filter(is_key=True)

    # Recuperation des 3 plus proches en prix
    #if len(better_prestations) > 2:
    #    better_prestations = better_prestations[len(better_prestations) - 3:len(better_prestations) - 1]

    # Serialisation
    better_prestations = [model_to_dict(p) for p in better_prestations]
    prestations = [dict(zip(included_keys, [p[k] for k in included_keys])) for p in better_prestations]

    prestations.append(model_to_dict(prestation))

    # Comblage avec des retours moins interessants
    if len(prestations) < 6:
        worst_prestations = Prestation.objects.annotate(Min('price')).order_by('price').filter(offers=prestation.offers, \
                                            price__gt=prestation.price, \
                                            provider__in=prestation.elligibility.split('|'), \
                                            is_phone_credit=prestation.is_phone_credit)[:5-len(prestations)]
        worst_prestations = [model_to_dict(p) for p in worst_prestations]
        prestations.extend([dict(zip(included_keys, [p[k] for k in included_keys])) for p in worst_prestations])

    return prestations

############
#   APIS
############

def delete(request):
    if request.is_ajax() or request.method == 'POST':
        try:
            json_data = json.loads(request.body)
            if 'identifier' in json_data and json_data['identifier'] != '':
                prestation = Prestation.objects.get(identifier=json_data['identifier'])
                prestation.delete()
                ajaxReturn = AjaxReturn("OK", {})
            else:
                ajaxReturn = AjaxReturn("KO", {}, "Prestation absente de la requête.")
        except Exception as e:
            logger.error('Une erreur est survenue : %s' % e.message)
            ajaxReturn = AjaxReturn("KO", {}, e.message)
        return HttpResponse(json.dumps(ajaxReturn.__dict__, cls=DatetimeEncoder), mimetype="application/json")

    return redirect('homepage')

def get_stats(request):
    if request.is_ajax() or request.method == 'POST':
        try:
            # Parsing requete
            json_data = json.loads(request.body)
            # Recuperation donnees
            prestations = get_stats_datas(json_data['identifier'])
            # Retour OK
            ajaxReturn = AjaxReturn("OK", prestations)

        except Exception as e:
            logger.error('Une erreur est survenue : %s' % e.message)
            ajaxReturn = AjaxReturn("KO", {}, e.message)
        
        return HttpResponse(json.dumps(ajaxReturn.__dict__, cls=DatetimeEncoder), mimetype="application/json")
    
    return redirect('homepage')


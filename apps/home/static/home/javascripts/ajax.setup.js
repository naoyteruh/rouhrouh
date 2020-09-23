(function($){
	$.fn.apiCall = function(url, callback) {
      $.ajax({
        type: 'GET',
        url: url,
        success: callback
      });
  };
})(jQuery);

(function($){
  $.fn.apiPost = function(url, data, callback) {
      $.ajax({
        type: 'POST',
        data: data,
        url: url,
        success: callback
      });
  };
})(jQuery);

(function($){

  $.fn.parseAjaxReturn = function(ajaxReturn) {
    var json;
    if(typeof(ajaxReturn.status)!=='undefined') {
        json = ajaxReturn;
    }
    else
    {
        json = JSON.parse(ajaxReturn);
    }
    return json;
  };

})(jQuery);

(function($){
    $.fn.processAjaxReturn = function(ajaxReturn, functionOk, functionKo) {
        var json = $.fn.parseAjaxReturn(ajaxReturn);
        if (json.status == 'OK')
        {
            functionOk(json);
        }
        else
        {
            functionKo(json);
        }
    };
    $.fn.processAjaxReturn2 = function(ajaxReturn) {
        var json = $.fn.parseAjaxReturn(ajaxReturn);
        if (json.status != 'OK')
        {
            throw "";
        }
        return json;
    };

})(jQuery);

$(document).ready(function(){    
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }         
    var csrftoken = getCookie('csrftoken');      
    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }                                       
    function sameOrigin(url) {
        // test that a given url is a same-origin URL
        // url could be relative or scheme relative or absolute
        var host = document.location.host; // host + port
        var protocol = document.location.protocol;
        var sr_origin = '//' + host;
        var origin = protocol + sr_origin;
        // Allow absolute or scheme relative URLs to same origin
        return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
            (url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
            // or any other URL that isn't scheme relative or absolute i.e relative.
            !(/^(\/\/|http:|https:).*/.test(url));
    }           
    $.ajaxSetup({
        contentType: 'application/json',
        error: function(x,e){
            if(x.status==0){
                console.log('Vous êtes hors ligne\n Vérifiez votre connectivité SVP.');
            }else if(x.status==404){
                console.log('URL non trouvée.');
            }else if(x.status==500){
                console.log('Erreur Interne.');
            }else if(e=='parsererror'){
                console.log('Erreur.\nParamètres incorrects.');
            }else if(e=='timeout'){
                console.log('Temps dépassé.');
            }else {
                console.log('Erreur Inconnue.\n'+x.responseText);
            }
        },
        dataType: 'json',
        processData: false,
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && sameOrigin(settings.url)) {
                // Send the token to same-origin, relative URLs only.
                // Send the token only if the method warrants CSRF protection
                // Using the CSRFToken value acquired earlier
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });
});



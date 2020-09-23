
/**
 * @param  {[type]}
 * @return {[type]}
 */
(function($){

    /**
     * Retourne une ligne de tableau à partir d un prestation
     * @param  {[type]}
     * @param  {[type]}
     * @param  {Boolean}
     * @param  {Boolean}
     * @return {[type]}
     */
	$.fn.getPrestationSummaryTable = function(index, prestation, isMobile, hasCommitment)
    {
        var result = "";
        var isLargeDisplay = $(window).width() > 768;

        // Ligne standard
        result += "<tr class='row-table " + ( index % 2 ? "even": "odd" ) + "'>";
        result += "<td data-toggle='collapse' data-target='#row-detail-" + index + "'>" + providers[prestation.provider] + "</td>";
        result += "<td>" + offers[prestation.offers] + "</td>";

        if (isMobile) {
        
            result += "<td class='large-display col-mobile'>" + $.fn.humabool(prestation.is_sms_unlimited) + "</td>"; 
            result += "<td class='large-display col-mobile'>" + $.fn.humabool(prestation.is_mms_unlimited) + "</td>";
            result += "<td class='large-display col-mobile'>" + $.fn.humabool(prestation.is_4g) + "</td>";
            result += "<td class='large-display col-mobile'>" + $.fn.humabool(prestation.is_key) + "</td>";
            result += "<td class='large-display col-mobile'>" + $.fn.humabool(prestation.is_blocked) + " </td>";
            result += "<td class='large-display col-mobile'>" + $.fn.humabool(prestation.is_phone_credit) + "</td>";
            if (hasCommitment) {
                result += "<td class='large-display col-subscription'>" + commitments[prestation.commitment] + "</td>";
                result += "<td class='large-display col-subscription'>" + (typeof(prestation.subscription) !== 'undefined' ? prestation.subscription : "Non d&eacute;finie") + "</td>";
            }
            if (prestation.data_offers != 'autre') {
                result += "<td class='large-display col-mobile'>" + data_offers[prestation.data_offers] + "</td>";
            }
            else {
                result += "<td class='large-display col-mobile'>" + prestation.data+ "</td>";
            }
        }
        
        result += "<td class='large-display'>"+ $.fn.humabool(prestation.fidelity) +"</td>";
        
        result += "<td>" + $.fn.decimalize(prestation.price) + "\u20AC</td>"; 
        result += "</tr>"

        // Ligne de détail
        result += "<tr id='row-detail-" + index + "' class='row-detail collapse out'>";
        result += "<td colspan=3 class='visible-xs visible-sm visible-md'>";
        result += "<div>";

        if (isMobile) {
            
            result += "SMS illimit&eacute;s : " + $.fn.humabool(prestation.is_sms_unlimited) + "<br >"; 
            result += "MMS illimit&eacute;s : " + $.fn.humabool(prestation.is_mms_unlimited) + "<br>";
            result += "4G : " + $.fn.humabool(prestation.is_4g) + "<br>";
            result += "Acc&egrave;s ordinateur : " + $.fn.humabool(prestation.is_key) + "<br>";
            result += "Bloqu&eacute; : " + $.fn.humabool(prestation.is_blocked) + " <br>";
            result += "Remboursement : " + $.fn.humabool(prestation.is_phone_credit) + "<br>";
            if (hasCommitment) {
                result += "Engagement :" + commitments[prestation.commitment] + "<br>";
                result += "Date de soucription : " + (typeof(prestation.subscription) !== 'undefined' ? prestation.subscription : "Non définie") + "<br>";
            }
            if (prestation.data_offers != 'autre') {
                result += "Datas : " + data_offers[prestation.data_offers] + "<br>";
            }
            else {
                result += "Datas : " + prestation.data+ "<br>";
            }
        }
        
        result += "Avantages fidelit&eacute; : "+ $.fn.humabool(prestation.fidelity) +"<br>";
        result += "</div>";
        result += "</td>";
        result += "</tr>";
        return result;        
    };

})(jQuery);

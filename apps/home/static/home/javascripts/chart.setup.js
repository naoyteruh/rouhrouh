(function($){


	Chart.types.Bar.extend({
	    name: "CustomBar",

	    chartTitle: "",

	    draw: function () {
	        Chart.types.Bar.prototype.draw.apply(this, arguments);

	        var ctx = this.chart.ctx;
	        ctx.save();

	        // text alignment and color
	        ctx.textAlign = "center";
	        ctx.textBaseline = "bottom";
	        //ctx.fillStyle = this.options.scaleFontColor;
	        ctx.fillStyle = "#409EFF";
	        ctx.lineWidth = 2;

	        var x = this.chart.width / 2;
	        var y = this.chart.height / 5;
	        ctx.translate(x, y)
	        ctx.fillText(this.options.chartTitle, 0, 0);

	        /*
	        x = this.scale.xScalePaddingLeft * 0.4;
	        y = this.chart.height / 2;
	        ctx.translate(x, y)
	        ctx.rotate(-90 * Math.PI / 180);
	        ctx.fillText(this.datasets[0].label, 0, 0);
	        */
	        ctx.restore();

	    }
	});

	$.fn.otherDataset = function(label, valueset) {
        return {  
        	label : label,          
            fillColor : "rgba(115,184,255,0.5)",
            strokeColor : "rgba(0,81,166,0.8)",
            highlightFill: "rgba(115,184,255,0.75)",
            highlightStroke: "rgba(0,81,166,1)",
            data : valueset
        }
    };

    $.fn.userDataset = function(label, valueset) {
        return {
        	label : label,             
            fillColor : "rgba(255,184,115,0.5)",
            strokeColor : "rgba(0,81,166,0.8)",
            highlightFill: "rgba(115,184,255,0.75)",
            highlightStroke: "rgba(0,81,166,1)",
            data : valueset
        }
    };

	$.fn.initChart = function(chartTitle, labels, datasets) {

        var barChartData = {
            labels : [],
            datasets : []
        }

        barChartData.labels = labels;
        $.each(datasets, function(index, valueset) {
            barChartData.datasets.push(valueset);
        });

	    var chartCtx = document.getElementById("canvas").getContext("2d");

        if (typeof(window.myBar) !== 'undefined') {
            window.myBar.destroy();
        }        
	    // chartCtx.canvas.height = ($("#canvas-holder").height() / 2) - 30;
	    // chartCtx.canvas.width = ($("#canvas-holder").width() / 2) - 30;
        // chartCtx.canvas.height = $("#canvas-holder").height() - 30;
        // chartCtx.canvas.width = $("#canvas-holder").width() - 30;
        //chartCtx.canvas.prop({ width: 700, height: 400 });

        window.myBar = new Chart(chartCtx).CustomBar(barChartData, {

            chartTitle: chartTitle,

            // Boolean - Whether to animate the chart
            animation: true,

            // Number - Number of animation steps
            animationSteps: 60,

            // String - Animation easing effect
            // Possible effects are:
            // [easeInOutQuart, linear, easeOutBounce, easeInBack, easeInOutQuad,
            //  easeOutQuart, easeOutQuad, easeInOutBounce, easeOutSine, easeInOutCubic,
            //  easeInExpo, easeInOutBack, easeInCirc, easeInOutElastic, easeOutBack,
            //  easeInQuad, easeInOutExpo, easeInQuart, easeOutQuint, easeInOutCirc,
            //  easeInSine, easeOutExpo, easeOutCirc, easeOutCubic, easeInQuint,
            //  easeInElastic, easeInOutSine, easeInOutQuint, easeInBounce,
            //  easeOutElastic, easeInCubic]
            animationEasing: "easeOutQuart",

            // Boolean - If we should show the scale at all
            showScale: true,

            // Boolean - If we want to override with a hard coded scale
            scaleOverride: false,

            // ** Required if scaleOverride is true **
            // Number - The number of steps in a hard coded scale
            scaleSteps: null,
            // Number - The value jump in the hard coded scale
            scaleStepWidth: null,
            // Number - The scale starting value
            scaleStartValue: null,

            // String - Colour of the scale line
            scaleLineColor: "rgba(0,0,0,.1)",

            // Number - Pixel width of the scale line
            scaleLineWidth: 1,

            // Boolean - Whether to show labels on the scale
            scaleShowLabels: true,

            // Interpolated JS string - can access value
            scaleLabel: "<%=value%>",

            // Boolean - Whether the scale should stick to integers, not floats even if drawing space is there
            scaleIntegersOnly: true,

            // Boolean - Whether the scale should start at zero, or an order of magnitude down from the lowest value
            scaleBeginAtZero: false,

            // String - Scale label font declaration for the scale label
            scaleFontFamily: "'Verdana'",

            // Number - Scale label font size in pixels
            scaleFontSize: 15,

            // String - Scale label font weight style
            scaleFontStyle: "bold",

            // String - Scale label font colour
            scaleFontColor: "#409EFF",

            // Boolean - Determines whether to draw tooltips on the canvas or not
            showTooltips: true,

            // Function - Determines whether to execute the customTooltips function instead of drawing the built in tooltips (See [Advanced - External Tooltips](#advanced-usage-external-tooltips))
            customTooltips: false,
            /*
			customTooltips: function(tooltip) {

				var tooltipEl = $('#canvas-tooltip');

				// Hide if no tooltip
		        if (!tooltip) {
		            tooltipEl.css({
		                opacity: 0
		            });
		            return;
		        }

		        // tooltip will be false if tooltip is not visible or should be hidden
		        if (!tooltip) {
		            return;
		        }

		        console.log(tooltip);

		        tooltipEl.html(tooltip.text);

		        // Find Y Location on page
		        var top;
		        if (tooltip.yAlign == 'above') {
		            top = tooltip.y - tooltip.caretHeight - tooltip.caretPadding;
		        } else {
		            top = tooltip.y + tooltip.caretHeight + tooltip.caretPadding;
		        }

		        // Display, position, and set styles for font
		        tooltipEl.css({
		            opacity: 1,
		            left: tooltip.chart.canvas.offsetLeft + tooltip.x + 'px',
		            top: tooltip.chart.canvas.offsetTop + top + 'px',
		            fontFamily: tooltip.fontFamily,
		            fontSize: tooltip.fontSize,
		            fontStyle: tooltip.fontStyle,
		        });

		    },
		    */


            // Array - Array of string names to attach tooltip events
            tooltipEvents: ["mousemove", "touchstart", "touchmove"],

            // String - Tooltip background colour
            tooltipFillColor: "rgba(0,0,0,0.8)",

            // String - Tooltip label font declaration for the scale label
            tooltipFontFamily: "'Helvetica Neue', 'Helvetica', 'Arial', sans-serif",

            // Number - Tooltip label font size in pixels
            tooltipFontSize: 14,

            // String - Tooltip font weight style
            tooltipFontStyle: "normal",

            // String - Tooltip label font colour
            tooltipFontColor: "#fff",

            // String - Tooltip title font declaration for the scale label
            tooltipTitleFontFamily: "'Helvetica Neue', 'Helvetica', 'Arial', sans-serif",

            // Number - Tooltip title font size in pixels
            tooltipTitleFontSize: 14,

            // String - Tooltip title font weight style
            tooltipTitleFontStyle: "bold",

            // String - Tooltip title font colour
            tooltipTitleFontColor: "#fff",

            // String - Tooltip title template
            tooltipTitleTemplate: "<%= label%>",

            // Number - pixel width of padding around tooltip text
            tooltipYPadding: 6,

            // Number - pixel width of padding around tooltip text
            tooltipXPadding: 6,

            // Number - Size of the caret on the tooltip
            tooltipCaretSize: 8,

            // Number - Pixel radius of the tooltip border
            tooltipCornerRadius: 6,

            // Number - Pixel offset from point x to tooltip edge
            tooltipXOffset: 10,

            // String - Template string for single tooltips
            tooltipTemplate: "<%if (label){%><%=label%>: <%}%><%= value %> euros",

            // String - Template string for multiple tooltips
            //multiTooltipTemplate: "<%= value %>",
            multiTooltipTemplate: "<%= datasetLabel %>: <%= value %>",

            // Function - Will fire on animation progression.
            onAnimationProgress: function(){},

            // Function - Will fire on animation completion.
            onAnimationComplete: function(){},

            //Boolean - Whether the scale should start at zero, or an order of magnitude down from the lowest value
            scaleBeginAtZero : true,

            //Boolean - Whether grid lines are shown across the chart
            scaleShowGridLines : true,

            //String - Colour of the grid lines
            scaleGridLineColor : "rgba(0,0,0,.05)",

            //Number - Width of the grid lines
            scaleGridLineWidth : 3,

            //Boolean - Whether to show horizontal lines (except X axis)
            scaleShowHorizontalLines: true,

            //Boolean - Whether to show vertical lines (except Y axis)
            scaleShowVerticalLines: true,

            //Boolean - If there is a stroke on each bar
            barShowStroke : true,

            //Number - Pixel width of the bar stroke
            barStrokeWidth : 2,

            //Number - Spacing between each of the X value sets
            barValueSpacing : 5,

            //Number - Spacing between data sets within X values
            barDatasetSpacing : 1,

            //String - A legend template
            legendTemplate : "<ul class=\"<%=name.toLowerCase()%>-legend\"><% for (var i=0; i<datasets.length; i++){%><li><span style=\"background-color:<%=datasets[i].fillColor%>\"><%if(datasets[i].label){%><%=datasets[i].label%><%}%></span></li><%}%></ul>",

            // Affichage responsive
            responsive : true,

            // Boolean - whether to maintain the starting aspect ratio or not when responsive, if set to false, will take up entire container
            maintainAspectRatio: true,
        });
        
	};

})(jQuery);
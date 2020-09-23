jQuery(document).ready(function ($) {

	$.stellar.scrollProperty.margin = {
      getLeft: function($element) {
      },
      getTop: function($element) {
        return parseInt($element.scrollLeft(), 10) * -1;
      }
    }
    $(window).stellar({
        // Set scrolling to be in either one or both directions
        horizontalScrolling: false,
        verticalScrolling: true,
        // Set the global alignment offsets
        horizontalOffset: 0,
        verticalOffset: 0,
        // Refreshes parallax content on window load and resize
        responsive: true,
        // Select which property is used to calculate scroll.
        // Choose 'scroll', 'position', 'margin' or 'transform',
        // or write your own 'scrollProperty' plugin.
        //scrollProperty: 'margin',
        scrollProperty: 'scroll',
        // Select which property is used to position elements.
        // Choose between 'position' or 'transform',
        // or write your own 'positionProperty' plugin.
        positionProperty: 'position',
        // Enable or disable the two types of parallax
        parallaxBackgrounds: true,
        parallaxElements: true,
        // Hide parallax elements that move outside the viewport
        //BUG
        hideDistantElements: true
        //hideDistantElements: false
    });

});
/*
Project:  White Space
Version:  1.0
Primary use:  Personal, Portfolio, Resume
Developed By: Reejo George
*/

(function ($) {
    "use strict";

/* QueryLoader2 */

    window.addEventListener('DOMContentLoaded', function() {
    new QueryLoader2(document.querySelector("body"), {
            barColor: "#5a5a5a", //background color of the bar (in hex). Default: "#FFF"
            backgroundColor: "#fff", //background color of the loader (in hex). Default: "#000"
            percentage: false, //Set to true to enable percentage visualising. Default: false
            barHeight: 2, //height of the bar in pixels. Default: 1
            bar: false,  
            minimumTime: 500, //time in miliseconds which the loading has to run. If time has not passed the animation will still show. 
            fadeOutTime: 1000 //time in miliseconds it takes for the overlay to fade out at the end. Default: 1000
        });
    });

    $('#nav').onePageNav({
        currentClass: 'current',
        changeHash: false,
        scrollSpeed: 750,
        scrollThreshold: 0.5,
        filter: '',
        easing: 'swing'
    });

/*Document Ready Functions Start*/

$(document).ready(function() {


  function setHeight() {
    var windowHeight = $(window).innerHeight();
    $('.intro').css('min-height', windowHeight);
  };
  setHeight();
  
  $(window).resize(function() {
    setHeight();
  });
  
    $('.skillbar').each(function() {
      $(this).appear(function() {
        $(this).find('.count-bar').animate({
          width:$(this).attr('data-percent')
        },3000);
        var percent = $(this).attr('data-percent');
        $(this).find('.count').html('<span>' + percent + '</span>');
      });
    });

    $(function() {
            //Initialize filterizr with default options
            $('#isotopeGrid').filterizr();
            $('.filters-group li .filter').on('click', function() {
            $('.filters-group li .filter').removeClass('is-checked');
            $(this).addClass('is-checked');
    });
    });

    /*OwlCarousels Start*/

     $('#experience').owlCarousel({

    loop:true,
    margin:40,
    nav:false,
    pagination:true,
    navigation:true,
    autoplay:true,
    autoplayTimeout:5000,
    autoplayHoverPause:true,
    responsive:true,
    responsive:{
        0:{
            items:1
        },
 
        983:{
            items:1
        },

       1100:{
            items:2
        }
    }
});

   $('#academic').owlCarousel({

    loop:true,
    margin:40,
    nav:false,
    pagination:true,
    navigation:true,
    autoplay:true,
    autoplayTimeout:5000,
    autoplayHoverPause:true,
    responsive:true,
    responsive:{
        0:{
            items:1
        },
 
        983:{
            items:1
        },

       1100:{
            items:2
        }
    }
});

    $('#portfolio-slide').owlCarousel({
    loop:true,
    nav:false,
    pagination:true,
    navigation:true,
    autoplay:true,
    autoplayTimeout:5000,
    autoplayHoverPause:true,
    items:1
});

  /*OwlCarousels End*/

  //.parallax(xPosition, speedFactor, outerHeight) options:
  //xPosition - Horizontal position of the element
  //inertia - speed to move relative to vertical scroll. Example: 0.1 is one tenth the speed of scrolling, 2 is twice the speed of scrolling
  //outerHeight (true/false) - Whether or not jQuery should use it's outerHeight option to determine when a section is in the viewport
$('.parallax').parallax({ "coeff":+0.2 });

});
 
/*Document Ready Functions End*/


  $('#nav-icon').on('click', function(){
    $(this).toggleClass('open');
    $('#headerBar').toggleClass('is-active');
  });
  $('.col-left ul li a').on('click', function(){
    $('#headerBar').removeClass('is-active');
    $('#nav-icon').removeClass('open');
  });


var stickyNavTop = $( 'body' ).offset().top + 250;
var stickyNav = function ()
        {
             var scrollTop = $( window ).scrollTop(); if ( scrollTop > stickyNavTop ){
              $("#headMobile").addClass("is-active");
              $("#nav-icon").addClass("active-nav");
             } else{
              $("#headMobile").removeClass("is-active");
              $("#nav-icon").removeClass("active-nav");
             }
         };
         stickyNav();
         $( window ).scroll( function (){
           stickyNav();
         });

// --------- Google Map init ----------  //
// When the window has finished loading create our google map below
google.maps.event.addDomListener(window, 'load', init);
        
function init() {
 // Basic options for a simple Google Map
// For more options see: https://developers.google.com/maps/documentation/javascript/reference#MapOptions
var mapOptions = {
// How zoomed in you want the map to start at (always required)
zoom: 9,
// Disable mouse scroll wheel scaling on Google Maps
scrollwheel: false,
// The latitude and longitude to center the map (always required)
center: new google.maps.LatLng(40.712784, -74.005941), // New York
//Find your latitude and longitude: http://www.latlong.net/
// How you would like to style the map. 
// This is where you would paste any style found on Snazzy Maps.
styles: [{"featureType":"administrative","elementType":"labels.text.fill","stylers":[{"color":"#444444"}]},{"featureType":"landscape","elementType":"all","stylers":[{"color":"#f2f2f2"}]},{"featureType":"poi","elementType":"all","stylers":[{"visibility":"off"}]},{"featureType":"road","elementType":"all","stylers":[{"saturation":-100},{"lightness":45}]},{"featureType":"road.highway","elementType":"all","stylers":[{"visibility":"simplified"}]},{"featureType":"road.arterial","elementType":"labels.icon","stylers":[{"visibility":"off"}]},{"featureType":"transit","elementType":"all","stylers":[{"visibility":"off"}]},{"featureType":"water","elementType":"all","stylers":[{"color":"#ffffff"},{"visibility":"on"}]}]
                };
// Get the HTML DOM element that will contain your map 
// We are using a div with id="map" seen below in the <body>
var mapElement = document.getElementById('map');
// Create the Google Map using our element and options defined above
var map = new google.maps.Map(mapElement, mapOptions);
// Let's also add a marker while we're at it
var marker = new google.maps.Marker({
 position: new google.maps.LatLng(9.931233, 76.267304),
 map: map,
 title: 'Snazzy!'
 });
} 

})(jQuery);
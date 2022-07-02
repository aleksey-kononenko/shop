$(document).ready(function () {




    /*==================================
     Parallax Effect for Home page
     ====================================*/

    if (/Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent)) {
    } else {



        // Tiny jQuery Plugin
        // by Chris Goodchild
        $.fn.exists = function (callback) {
            var args = [].slice.call(arguments, 1);

            if (this.length) {
                callback.call(this, args);
            }

            return this;
        };

        // Usage Parallax 
        $('.parallax-image-1').exists(function () {

            //alert('1 here');
            var offsetParallax1 = $(".parallax-image-1").offset().top;
            $('.parallax-image-1').parallax("50%", offsetParallax1, 0.1, true);

        });

        $('.parallax-image-2').exists(function () {

            //alert('2 here');
            var offsetParallax2 = $(".parallax-image-2").offset().top;
            $('.parallax-image-2').parallax("50%", offsetParallax2, 0.1, true);

        });


    } // mobile userAgent end 


    /*==================================
     Home Page Slider  || jQuery Cycle
     ====================================*/


    $('.slider-v1').cycle({
        //Specify options
        fx: 'scrollHorz',
        //Name of transition effect 
        slides: '.slider-item',
        timeout: 5000,
        // set time for nex slide 
        speed: 1200,
        easeIn: 'easeInOutExpo',
        // easing 
        easeOut: 'easeInOutExpo',
        pager: '#pager2',
        //Selector for element to use as pager container 
    });


    // show loading image
    $('#loader_img').show();

    // main image loaded 
    $('.sliderImg').load(function () {
        // hide/remove the loading image
        $('#loader_img').hide();
    });

    /*==================================
     Carousel
     ====================================*/

    // NEW ARRIVALS Carousel

    function customPager() {

        $.each(this.owl.userItems, function (i) {

            var pagination1 = $('.owl-controls .owl-pagination > div:first-child');
            var pagination = $('.owl-controls .owl-pagination');
            $(pagination[i]).append("<div class=' owl-has-nav owl-next'><i class='fa fa-angle-right'></i>  </div>");
            $(pagination1[i]).before("<div class=' owl-has-nav owl-prev'><i class='fa fa-angle-left'></i> </div>");


        });

    }

    var latestProductSlider = $("#productslider");

    latestProductSlider.owlCarousel({
        navigation: false, // Show next and prev buttons
        items: 4,
        itemsTablet: [768, 2],
        afterInit: customPager,
        afterUpdate: customPager
    });


    // Custom Navigation Events
    $(".owl-next").click(function () {
        latestProductSlider.trigger('owl.next');
        console.log('next');
    })
    $(".owl-prev").click(function () {
        latestProductSlider.trigger('owl.prev');
        console.log('previous');
    })


}); // end Ready
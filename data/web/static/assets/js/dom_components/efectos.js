$(document).ready(function () {
    if ( $(window).width()>800) {
        $('header .titulo').css({
            opacity: 0,
            marginTop: '52px'                        
        });
        $('header .titulo').animate({
            opacity: 1,
            marginTop: '0px'
        }, 1500);
    }
})
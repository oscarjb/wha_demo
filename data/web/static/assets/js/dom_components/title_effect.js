$(document).ready(function () {
    if ( $(window).width()>800) {
        $('header .title').css({
            opacity: 0,
            marginTop: '52px'                        
        });
        $('header .title').animate({
            opacity: 1,
            marginTop: '0px'
        }, 1500);
    }
})
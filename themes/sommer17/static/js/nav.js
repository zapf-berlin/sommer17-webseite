$(document).ready(function() {
var stickyNavTop = $('.main-menu').offset().top;

var stickyNav =
function(){
    var scrollTop = $(window).scrollTop();

    if (scrollTop > stickyNavTop) {
        $('.main-menu').addClass('sticky');
	$('.menuhidden').css({"position":"fixed"});
    } else {
        $('.main-menu').removeClass('sticky');
	$('.menuhidden').css({"position":"absolute"});
    }
};

stickyNav();

$(window).scroll(function() {
	stickyNav();
});
});

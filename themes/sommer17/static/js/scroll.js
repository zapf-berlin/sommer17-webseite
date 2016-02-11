function compute_offset() {
	return 0.1*$('#header-image').outerHeight();
}
function compute_duration() {
	/* Set the duration according to the height of the image */
	return $('#header-image').outerHeight()-compute_offset() -12;
}

var scene = new ScrollMagic.Scene({offset: compute_offset(), duration: compute_duration(), triggerHook: 0})
	.on("enter", function (e) {

		if (e.target.controller().info("scrollDirection") == "FORWARD") {
			$('html, body').animate({scrollTop: ($('#main-menu').offset().top)}, 400, 'swing', function() {
				$('#main-menu').addClass('pinned');
			});
			scene['duration'](compute_duration());
		} else {
			$('#main-menu').removeClass('pinned');
			$('html, body').animate({scrollTop: 0}, 'slow');
		}
	})
	.addTo(scroller);


/* Ensure the body is large enough */
function minimum_resize() {
		var minimum_height = $(window).height() - $('#main-footer').outerHeight();

		//var minimum_height = 10000;
		if ($('#main-content').outerHeight() < minimum_height) {
			$('#main-content').height(minimum_height);
		}
}

$(window).on('resize', minimum_resize);
$(minimum_resize);
$(window).on('resize', function() {scene['duration'](compute_duration());});
$(window).on('resize', function() {scene['offset'](compute_offset());});

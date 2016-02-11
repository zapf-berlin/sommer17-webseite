function compute_offset() {
	return $('#header-image').outerHeight();
}

var scene = new ScrollMagic.Scene({offset: compute_offset(), triggerHook: 0})
	.on("enter", function (e) {
		$('#main-menu').addClass('pinned');
		scene['offset'](compute_offset());
	})
	.on("leave", function (e) {
		$('#main-menu').removeClass('pinned');
		scene['offset'](compute_offset());
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
$(window).on('resize', function() {scene['offset'](compute_offset());});

var pin_navigation = new ScrollMagic.Scene({triggerElement: '#submenu', triggerHook: 0.25})
	.setPin('#submenu', {spacerClass: 'submenu-spacer'})
  .addTo(scroller);

$(document).ready(function() {

	// $("#headshot").mouseenter(function () {
	// 	$("#headshot div").animate({
	// 		opacity: 0.75
	// 	}, 250);
	// });

	// $("#headshot").mouseleave(function () {
	// 	$("#headshot div").animate({
	// 		opacity: 0
	// 	}, 250);
	// });


	$(".section-link").click(function(e) {
		var elementId = e.target;

		$("html, body").animate({
			scrollTop: $(elementId).offset().scrollTop;
		}, 500);
		// return false;
	});

});

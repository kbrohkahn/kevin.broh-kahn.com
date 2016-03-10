$(document).ready(function() {
	$("#headshot").mouseenter(function () {
		$("#headshot div").animate({
			opacity: 0.5
		}, 250);
	});

	$("#headshot").mouseleave(function () {
		$("#headshot div").animate({
			opacity: 0
		}, 250);
	});
	
});

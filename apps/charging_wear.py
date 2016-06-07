#!/usr/bin/env python
with open("../templates/header.html", "r") as header:
	print header.read()
with open("../templates/navbar.html", "r") as navbar:
	print navbar.read()

print("""
<div class="row">
	<div class="col-xxs-6 col-xxs-offset-3 col-xs-4 col-sm-3 col-md-2 col-lg-1">
		<img class="img-responsive" alt="Charging Wear Icon" src="/assets/img/charging_wear/icon.png">
	</div>
	<div class="col-xxs-12 col-xs-6 col-sm-9 col-md-10 col-lg-11">
		<h1>Charging Wear <small><a target="_blank" href="https://play.google.com/store/apps/details?id=com.bkmobiledevelopment.chargingwear">Google Play</a></small></h1>
		<div class="subheader">Control what your Android Wear smartwatch does while it's charging.</div>
	</div>
</div>
<h2>Description</h2>
<p class="indented">Charging Wear allows you to control how your smartwatch acts when it's charging. Normally, most Android wear devices do nothing but bring up a bright screen displaying the time and charging percentage. The feature can be annoying if you prefer sleeping without a nightlight and has the potential to cause screen burn.</p>
<p class="indented">Charging Wear has a simple but elegant solution to this dilemma.</p>
<p class="indented">To combat the charging screen issue, Charging Wear will show a completely black screen on your smartwatch whenever you plug your device in. This will allow for a peaceful, dark setting wherever you are charging your watch. The application also has the ability to turn off your watch's Bluetooth when it is charging. This ensures that the watch will not be connected to your phone when it is charging, because who wants their watch to vibrate when it's not on their wrist? Charging Wear also has the ability to take on many other features, simply email me if you have a request or any feedback!</p>
<p class="indented">Due to the youth of Android Wear and limited testing ability, I cannot guarantee that Charging Wear will function flawlessly on every device. If the app doesn't work, crashes, or looks ugly on your device, please send me an email and I'll look into your problem as soon as I can!</p>
<h2>Features</h2>
<ul>
	<li>Display dark screen while watch is charging</li>
	<li>Toggle Bluetooth while watch is charging</li>
</ul>

<h2>Screenshots</h2>
<div class="row screenshots">
	<div class="col-md-2 col-sm-3 col-xs-4">
		<img src="/assets/img/charging_wear/moto_360/screenshot_1.png" alt="Screenshot 1">
		<div>
			<em>Screenshot 1</em>
		</div>
	</div>
	<div class="col-md-2 col-sm-3 col-xs-4">
		<img src="/assets/img/charging_wear/moto_360/screenshot_2.png" alt="Screenshot 2">
		<div>
			<em>Screenshot 2</em>
		</div>
	</div>
	<div class="col-md-2 col-sm-3 col-xs-4">
		<img src="/assets/img/charging_wear/moto_360/screenshot_3.png" alt="Screenshot 3">
		<div>
			<em>Screenshot 3</em>
		</div>
	</div>
</div>

<h2>Download Charging Wear for free</h2>
<div class="badge-container">
	<a target="_blank" href="https://play.google.com/store/apps/details?id=com.bkmobiledevelopment.chargingwear">
		<img alt="Get it on Google Play" src="/assets/img/en_generic_rgb_wo_45.png" />
	</a>
</div>
""")

with open("../templates/footer.html", "r") as footer:
	print footer.read()

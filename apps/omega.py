#!/usr/bin/env python
with open("../templates/header.html", "r") as header:
	print header.read()
with open("../templates/navbar.html", "r") as navbar:
	print navbar.read()

print("""
<div class="row">
	<div class="col-xxs-6 col-xxs-offset-3 col-xs-4 col-sm-3 col-md-2 col-lg-1">
		<img class="img-responsive" alt="Omega Icon" src="/assets/img/charging_wear/icon.png">
	</div>
	<div class="col-xxs-12 col-xs-6 col-sm-9 col-md-10 col-lg-11">
		<h1>Omega Watch Face <small><a target="_blank" href="https://play.google.com/store/apps/details?id=com.brohkahn.omegawatchface">Google Play</a></small></h1>
		<div class="subheader">Complete video game themed watch face with battery, next event, and weather</div>
	</div>
</div>
<h2>Description</h2>
<p class="indented">Feel like the best secret agent while sporting the Omega watch face. You'll be able to leave your phone in your pocket as Omega will tell you every necessary detail you need to get through your day. By knowing your schedule with such details at a moment's glance, your friends might even think you to be a supernatural spy!</p>
<p class="indented">Omega is the most complete watch face for your Android Wear device. When fully utilized, Omega will tell you the time, date, weather, power level of your devices, and your next calendar event. Aside from the time and date (which we believe are the 2 requirements of all watch faces), these features are completely optional and customizable.</p>
<p class="indented">Purchase the paid version for only $.99 on <a target="_blank" href="https://play.google.com/store/apps/details?id=com.brohkahn.omega">Google Play</a></p>
<p class="indented"><h4>Application Issues:</h4></p>
<p class="indented">Our goal was to create a complete and fully functional, usable, power efficient watch face. If you do not think that our mission was a success, please send us an email at kevin@broh-kahn.com with your issues and we will get back to you as quickly as possible. If you have an issue with the application, please do not leave a negative review or uninstall the app; contact us and we will do our best to solve your issue within 3 days.</p>
<p class="indented"><h4>Feature Requests:</h4></p>
<p class="indented">If you have a small feature request (i.e. configuration change) for this watch face, please send us an email at kevin@broh-kahn.com and your request will be completed within 1 week, guaranteed. Larger requests may take more time. If you would like us to design a new watch face with all the functionality of Omega, please get in touch and we'll work with you to design a well-designed and functional watch face.</p>
<p class="indented"><h4>Device Support:</h4></p>
<p class="indented">We only had 1 device to test this watch face on, the Moto 360 Sport, so technically we can only guarantee that Omega will work on that device. If Omega does not work on your wearable device (which is possible) or your handheld device (which is less likely), please do not leave a negative review. We do not want you to be dissatisfied with our product, and if you installed this application you likely want a functional watch face you can use. Send us an email and we will do our best to get the application working on your device.</p>
<h2>Features</h2>
<ul>
	<li>Battery</li>
	<ul>
		<li>Show battery from your watch and/or phone, or if your devices have great battery life turn this feature off and enjoy the watch face design</li>
		<li>Choose the interval at which to poll the battery level of your devices</li>
		<li>Optionally show the exact battery life at the bottom of the screen (Paid version only), or just use the health monitors on the watch face to display battery life within 10% to 18%</li>
		<li>Use icons to show which device's battery is on which side of the screen, or turn off this feature if you have good memory or only wish to monitor 1 device</li>
		<li>Optionally show only the current health block in ambient mode to reduce screen burn-in and brightness</li>
	</ul>
	<li>Weather</li>
	<ul>
		<li>Omega's handheld app will get data from OpenWeatherMap at an interval of your choosing, the default setting is 30 minutes.</li>
		<li>Choose from a variety of details to show: the day's high & low, wind speed & direction, sunrise & sunset, or nothing for the minimalist look. (Paid version only)</li>
		<li>The handheld app uses your last reported location to determine the weather, therefore the handheld app requires your permission to access your location</li>
		<li>Temperature in Celsius / Fahrenheit</li>
	</ul>
	<li>Calendar</li>
	<ul>
		<li>Omega's wearable app will read the calendars that are on your wear device to determine your next event, and it requires your permission to do so</li>
		<li>Choose the interval at which to check for new events.</li>
		<li>As soon as your current event has ended, Omega will look for the next event.</li>
		<li>Choose how long in the future you want to look: check for event in the next 2 hours or the next 1 week.</li>
	</ul>
</ul>
<h2>Screenshots</h2>
<div class="row screenshots">
	<div class="col-md-2 col-sm-3 col-xs-4">
		<img src="/assets/img/omega/moto_360/screenshot_1.png" alt="Screenshot 1">
		<div>
			<em>Screenshot 1</em>
		</div>
	</div>
	<div class="col-md-2 col-sm-3 col-xs-4">
		<img src="/assets/img/omega/moto_360/screenshot_2.png" alt="Screenshot 2">
		<div>
			<em>Screenshot 2</em>
		</div>
	</div>
	<div class="col-md-2 col-sm-3 col-xs-4">
		<img src="/assets/img/omega/moto_360/screenshot_3.png" alt="Screenshot 3">
		<div>
			<em>Screenshot 3</em>
		</div>
	</div>
	<div class="col-md-2 col-sm-3 col-xs-4">
		<img src="/assets/img/omega/moto_360/screenshot_4.png" alt="Screenshot 4">
		<div>
			<em>Screenshot 4</em>
		</div>
	</div>
	<div class="col-md-2 col-sm-3 col-xs-4">
		<img src="/assets/img/omega/moto_360/screenshot_5.png" alt="Screenshot 5">
		<div>
			<em>Screenshot 5</em>
		</div>
	</div>
</div>

<h2>Download Omega for free</h2>
<div class="badge-container">
	<a target="_blank" href="https://play.google.com/store/apps/details?id=com.brohkahn.omegawatchface">
		<img alt="Get it on Google Play" src="/assets/img/en_generic_rgb_wo_45.png" />
	</a>
</div>

<h2>Purchase full version</h2>
<div class="badge-container">
	<a target="_blank" href="https://play.google.com/store/apps/details?id=com.brohkahn.omega">
		<img alt="Get it on Google Play" src="/assets/img/en_generic_rgb_wo_45.png" />
	</a>
</div>
""")

with open("../templates/footer.html", "r") as footer:
	print footer.read()

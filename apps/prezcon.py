#!/usr/bin/env python
with open("../templates/header.html", "r") as header:
	print header.read()
with open("../templates/navbar.html", "r") as navbar:
	print navbar.read()

print("""
<div class="row">
	<div class="col-xxs-6 col-xxs-offset-3 col-xs-4 col-sm-3 col-md-2 col-lg-1">
		<img class="img-responsive" alt="Prezcon Icon" src="/assets/img/prezcon/icon.png">
	</div>
	<div class="col-xxs-12 col-xs-8 col-sm-9 col-md-10 col-lg-11">
		<h1>Prezcon <small><a target="_blank" href="https://play.google.com/store/apps/details?id=com.prezcon.prezcon">Google Play</a></small></h1>
		<div class="subheader">The official application of the Prezcon Winter Nationals.</div>
	</div>
</div>
<h2>Features</h2>
<ul>
	<li>Offline storage of schedule (app does not require internet connection after download)</li>
	<li>View entire Prezcon schedule by day and hour</li>
	<li>View schedule of individual tournament</li>
	<li>Find rooms on hotel map</li>
	<li>Create personalized schedule for your week at the Prezcon Winter Nationals</li>
	<li>Add events to your individual schedule</li>
	<li>Filter tournaments and non-tournaments out of your schedule</li>
	<li>Edit and view all your tournament finishes</li>
	<li>Create and share notes for individual events</li>
</ul>
""")

with open("../templates/footer.html", "r") as footer:
	print footer.read()

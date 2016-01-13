#!/usr/bin/env python
with open("../templates/header.html", "r") as header:
	print header.read()
with open("../templates/navbar.html", "r") as navbar:
	print navbar.read()

print("""
<div class="row">
	<div class="col-xs-6 col-xs-offset-3 col-sm-offset-0 col-sm-3 col-md-2 col-lg-1">
		<img class="img-responsive" alt="WBC Icon" src="/assets/img/wbc/icon.png">
	</div>
	<div class="col-xs-12 col-sm-9 col-md-10 col-lg-11">
		<h1>WBC <small><a target="blank" href="https://play.google.com/store/apps/details?id=org.boardgamers.wbc">Google Play</a></small></h1>
		<div class="subheader">The official application of the World Boardgaming Championships.</div>
	</div>
</div>
<h2>Page under construction</h2>
""")

with open("../templates/footer.html", "r") as footer:
	print footer.read()

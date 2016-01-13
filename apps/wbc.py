#!/usr/bin/env python
with open("../templates/header.html", "r") as header:
	print header.read()
with open("../templates/navbar.html", "r") as navbar:
	print navbar.read()

print("""
<h1>WBC</h1>
<div class="subheader">The official application of the World Boardgaming Championships</div>
<div class="badge-container">
	<a target="blank" href="https://play.google.com/store/apps/details?id=org.boardgamers.wbc">
		<img alt="Get it on Google Play" src="/assets/img/en_generic_rgb_wo_45.png" />
	</a>
</div>
<h2>Page under construction</h2>
""")

with open("../templates/footer.html", "r") as footer:
	print footer.read()

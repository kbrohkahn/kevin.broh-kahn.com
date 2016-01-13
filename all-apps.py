#!/usr/bin/env python

with open("templates/header.html", "r") as header:
	print header.read()
with open("templates/navbar.html", "r") as navbar:
	print navbar.read()

print('<link href="/assets/css/circuit-background.css" rel="stylesheet">')

print("""
<div id="circuit-background">
	<div id="circuit-background-cover">
		<div class="center">
			<h4>Apps</h4>
			<ul class="link-list">
				<li><a href="/apps/ratfink">Ratfink</a></li>
				<li><a href="/apps/music_home">Music Home</a></li>
				<li><a href="/apps/wbc">WBC</a></li>
				<li><a href="/apps/prezcon">Prezcon</a></li>
			</ul>
		</div>
	</div>
</div>
""")

print('<script src="/assets/js/circuit-background-script.js" type="text/javascript"></script>')

with open("templates/footer.html", "r") as footer:
	print footer.read()

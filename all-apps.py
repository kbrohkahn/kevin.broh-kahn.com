#!/usr/bin/env python

with open("templates/header.html", "r") as header:
	print header.read()
with open("templates/navbar.html", "r") as navbar:
	print navbar.read()

print('<link href="/assets/css/circuit-background.css" rel="stylesheet">')

print("""
<div id="circuit-background">
	<div id="circuit-background-cover">
		<div class="navigation-links"">
			<a class="center" href="/all-apps"><h4>Apps</h4></a>
			<ul>
				<li><a href="/apps/ratfink"><img alt="Ratfink icon" class="small-icon" src="/assets/img/ratfink/icon.png">Ratfink</a></li>
				<li><a href="/apps/music_home"><img alt="Music Home icon" class="small-icon" src="/assets/img/music_home/icon.png">Music Home</a></li>
				<li><a href="/apps/wbc"><img alt="WBC icon" class="small-icon" src="/assets/img/wbc/icon.png">WBC</a></li>
				<li><a href="/apps/prezcon"><img alt="Prezcon icon" class="small-icon" src="/assets/img/prezcon/icon.png">Prezcon</a></li>
			</ul>
		</div>
	</div>
</div>
""")

print('<script src="/assets/js/circuit-background-script.js" type="text/javascript"></script>')

with open("templates/footer.html", "r") as footer:
	print footer.read()

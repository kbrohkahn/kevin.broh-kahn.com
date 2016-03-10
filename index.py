#!/usr/bin/env python

with open("templates/header.html", "r") as header:
	print header.read()

print('<link href="/assets/css/circuit-background.css" rel="stylesheet">')
print('<link href="/assets/css/index.css" rel="stylesheet">')

print("""
<div id="circuit-background">
	<span class="home-span left-triangle-span"></span>
	<span class="navigation-links">
		<a href="/apps"><h4>Apps</h4></a>
		<ul>
			<li><a href="/apps/ratfink"><img alt="Ratfink icon" class="small-icon" src="/assets/img/ratfink/icon.png"><span>Ratfink</span></a></li>
			<li><a href="/apps/music_home"><img alt="Music Home icon" class="small-icon" src="/assets/img/music_home/icon.png"><span>Music Home</span></a></li>
			<li><a href="/apps/wbc"><img alt="WBC icon" class="small-icon" src="/assets/img/wbc/icon.png"><span>WBC</span></a></li>
			<li><a href="/apps/prezcon"><img alt="Prezcon icon" class="small-icon" src="/assets/img/prezcon/icon.png"><span>Prezcon</span></a></li>
			<li><a href="/apps/charging_wear"><img alt="Charging Wear icon" class="small-icon" src="/assets/img/charging_wear/icon.png"><span>Charging Wear</span></a></li>
		</ul>
	</span>
	<span class="home-span right-triangle-span"></span>
	<span class="navigation-links">
		<a href="/projects"><h4>Projects</h4></a>
		<ul>
			<li><a href="/projects/view-recipes"><img alt="View Recipes icon" class="small-icon" src="/assets/img/view-recipes/icon.png"><span>View Recipes</span></a></li>
			<li><a href="/projects/website"><img alt="This website icon" class="small-icon" src="/assets/img/kevin.broh-kahn.com/icon.png"><span>This website</span></a></li>
		</ul>
	</span>
	<img id="headshot" class="img-circle" alt="My photo" src="/assets/img/headshot1.png">
</div>
""")

print('<script src="/assets/js/circuit-background-script.js" type="text/javascript"></script>')

with open("templates/footer.html", "r") as footer:
	print footer.read()

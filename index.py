#!/usr/bin/env python

with open("templates/header.html", "r") as header:
	print header.read()

print('<link href="/assets/css/circuit-background.css" rel="stylesheet">')
print('<link href="/assets/css/index.css" rel="stylesheet">')

print("""
<div id="circuit-background">
	<span class="home-span left-triangle-span"></span>
	<span class="navigation-links">
		<a href="/all-apps"><h4>Apps</h4></a>
		<ul>
			<li><a href="/apps/ratfink">Ratfink</a></li>
			<li><a href="/apps/music_home">Music Home</a></li>
			<li><a href="/apps/wbc">WBC</a></li>
			<li><a href="/apps/prezcon">Prezcon</a></li>
		</ul>
	</div>
	<span class="home-span right-triangle-span"></span>
	<span class="navigation-links">
		<a href="/all-projects"><h4>Projects</h4></a>
		<ul>
			<li><a href="/projects/view-recipes">View Recipes</a></li>
			<li><a href="/projects/website">This website</a></li>
		</ul>
	</span>
	<img id="headshot" class="img-circle" alt="My photo" src="/assets/img/headshot1.png">
</div>
""")

print('<script src="/assets/js/circuit-background-script.js" type="text/javascript"></script>')

with open("templates/footer.html", "r") as footer:
	print footer.read()

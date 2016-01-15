#!/usr/bin/env python

with open("templates/header.html", "r") as header:
	print header.read()
with open("templates/navbar.html", "r") as navbar:
	print navbar.read()

print('<link href="/assets/css/circuit-background.css" rel="stylesheet">')

print("""
<div id="circuit-background">
	<div id="circuit-background-cover">
		<div class="navigation-links">
			<h4 class="center">Contact Me</h4>
			<ul>
				<li><a class="no-icon" href="mailto:kbrohkahn@yahoo.com"><span>via email</span></a></li>
				<li><a class="no-icon" href="tel:410-487-4041"><span>via cell</span></a></li>
			</ul>
		</div>
	</div>
</div>
""")

print('<script src="/assets/js/circuit-background-script.js" type="text/javascript"></script>')

with open("templates/footer.html", "r") as footer:
	print footer.read()

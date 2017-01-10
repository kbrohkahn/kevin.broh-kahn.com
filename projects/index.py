#!/usr/bin/env python

with open("../templates/header.html", "r") as header:
	print header.read()
with open("../templates/navbar.html", "r") as navbar:
	print navbar.read()

print('<link href="/assets/css/circuit-background.css" rel="stylesheet">')

with open("index_contents.html", "r") as page_html:
	print page_html.read()

print('<script src="/assets/js/circuit-background-script.js" type="text/javascript"></script>')

with open("../templates/footer.html", "r") as footer:
	print footer.read()

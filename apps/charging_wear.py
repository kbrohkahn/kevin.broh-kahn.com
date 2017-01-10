#!/usr/bin/env python
with open("../templates/header.html", "r") as header:
	print header.read()
with open("../templates/navbar.html", "r") as navbar:
	print navbar.read()

with open("charging_wear_contents.html", "r") as page_html:
	print page_html.read()

with open("../templates/footer.html", "r") as footer:
	print footer.read()

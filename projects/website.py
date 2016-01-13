#!/usr/bin/env python
with open("../templates/header.html", "r") as header:
	print header.read()
with open("../templates/navbar.html", "r") as navbar:
	print navbar.read()

print("""
<h1>kevinbrohkahn.com</h1>
<div class="subheader">A site for displaying all of the projects and applications I have created</div>
<div class="center"><a target="blank" href="https://github.com/kbrohkahn/kevinbrohkahn.com">View project on Github</a></div>
""")

with open("../templates/footer.html", "r") as footer:
	print footer.read()

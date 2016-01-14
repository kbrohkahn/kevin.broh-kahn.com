#!/usr/bin/env python
with open("../templates/header.html", "r") as header:
	print header.read()
with open("../templates/navbar.html", "r") as navbar:
	print navbar.read()

print("""
<div class="row">
	<div class="col-xs-6 col-xs-offset-3 col-sm-offset-0 col-sm-3 col-md-2 col-lg-1">
		<img class="img-responsive" alt="kevinbrohkahn.com Icon" src="/assets/img/kevinbrohkahn.com/icon.png">
	</div>
	<div class="col-xs-12 col-sm-9 col-md-10 col-lg-11">
		<h1>kevinbrohkahn.com <small><a target="blank" href="https://github.com/kbrohkahn/kevinbrohkahn.com">Github</a></small></h1>
		<div class="subheader">A site for displaying all of the projects and applications I have created.</div>
	</div>
</div>
""")

with open("../templates/footer.html", "r") as footer:
	print footer.read()

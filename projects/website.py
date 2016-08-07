#!/usr/bin/env python
with open("../templates/header.html", "r") as header:
	print header.read()
with open("../templates/navbar.html", "r") as navbar:
	print navbar.read()

print("""
<div class="row">
	<div class="col-xxs-6 col-xxs-offset-3 col-xs-4 col-sm-3 col-md-2 col-lg-1">
		<img class="img-responsive" alt="kevin.broh-kahn.com Icon" src="/assets/img/kevin.broh-kahn.com/icon.png">
	</div>
	<div class="col-xxs-12 col-xs-8 col-sm-9 col-md-10 col-lg-11">
		<h1>kevin.broh-kahn.com <small><a target="_blank" href="https://bitbucket.org/kbrohkahn/kevin.broh-kahn.com">Bitbucket</a></small></h1>
		<div class="subheader">A site for displaying all of the projects and applications I have created.</div>
	</div>
</div>
""")

with open("../templates/footer.html", "r") as footer:
	print footer.read()

#!/usr/bin/env python
with open("../templates/header.html", "r") as header:
	print header.read()
with open("../templates/navbar.html", "r") as navbar:
	print navbar.read()

print("""
<div class="row">
	<div class="col-xxs-6 col-xxs-offset-3 col-xs-4 col-sm-3 col-md-2 col-lg-1">
		<img class="img-responsive" alt="sixsided.com Icon" src="/assets/img/sixsided.com/icon.png">
	</div>
	<div class="col-xxs-12 col-xs-8 col-sm-9 col-md-10 col-lg-11">
		<h1>Six Sided Simulations <small><a target="_blank" href="https://bitbucket.org/kbrohkahn/sixsided.com">Bitbucket</a></small></h1>
		<div class="subheader"><a target="_blank" href="https://sixsided.com">sixsided.com</a>, A site for viewing products and info by Six Sided Simulations.</div>
	</div>
</div>
<h2>Description</h2>
<p class="indented">Click <a target="_blank" href="https://sixsided.com">here</a> to visit Six Sided Simulations</p>
<p class="indented">I spent a few weekends updating sixsided.com to include the latest product by Six Sided Simulations, flag sheets for minatures. In doing so I also completely redesigned the website (which was a tad old) to be responsive and much faster.</p>
""")

with open("../templates/footer.html", "r") as footer:
	print footer.read()

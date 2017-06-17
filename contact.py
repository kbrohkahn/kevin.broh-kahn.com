#!/usr/bin/env python

with open("templates/header.html", "r") as header:
	print header.read()
with open("templates/navbar.html", "r") as navbar:
	print navbar.read()

print('<link href="/assets/css/circuit-background.css" rel="stylesheet">')

print("""
<div id="circuit-background"></div>

<div id="headers">
	<div class="logo" id="top-logo" href="/contact">
		<img alt="My logo" src="/assets/img/logo.png">
	</div>

	<div id="contact">
		<div class="subtitle">
			<h3>Get in Touch</h3>
		</div>

		<div class="links">
			<ul class="social-links">
				<li><a title="View my LinkedIn Profile" href="https://www.linkedin.com/in/kbrohkahn" target="_blank"><img src="/assets/img/social/LinkedIn-Icon.png"></a></li>
				<li><a title="View my Stack Overflow Profile" href="http://stackoverflow.com/cv/kbrohkahn" target="_blank"><img src="/assets/img/social/Stack-Overflow-Icon.png"></a></li>
				<li><a title="View my Bitbucket Profile" href="https://bitbucket.org/kbrohkahn/" target="_blank"><img src="/assets/img/social/Bitbucket-Icon.png"></a></li>
				<li><a title="View my GitHub Profile" href="https://github.com/kbrohkahn/" target="_blank"><img src="/assets/img/social/GitHub-Icon.png"></a></li>
				<li><a title="View my apps on the Google Play Store" href="https://play.google.com/store/apps/dev?id=4654453048954028942" target="_blank"><img src="/assets/img/social/Google-Play-Store-Icon.png"></a></li>
				<li><a title="View my apps on the App Store" href="https://itunes.apple.com/us/developer/kevin-broh-kahn/id1047274120" target="_blank"><img src="/assets/img/social/App-Store-Icon.png"></a></li>
			</ul>
			<ul>
				<li><a class="no-icon" href="mailto:kevin@broh-kahn.com"><span>Send me an email</span></a></li>
				<li><a class="no-icon" href="tel:410-487-4041"><span>Give me a call</span></a></li>
			</ul>
		</div>
	</div>

</div>
<script src="/assets/js/circuit-background-script.js" type="text/javascript"></script>
""")

with open("templates/footer.html", "r") as footer:
	print footer.read()

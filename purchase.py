#!/usr/bin/env python

with open("templates/header.html", "r") as header:
	print header.read()
with open("templates/navbar.html", "r") as navbar:
	print navbar.read()

print('<link href="/assets/css/circuit-background.css" rel="stylesheet">')

print("""
<div id="circuit-background">
	<div id="circuit-background-cover">
		<form action="https://www.paypal.com/cgi-bin/webscr" method="post" target="_top">
			<input type="hidden" name="cmd" value="_s-xclick">
			<input type="hidden" name="hosted_button_id" value="SB6K6DUK7VWF4">
			<table>
				<tr><td><input type="hidden" name="on0" value="Operating System">Operating System</td></tr>
				<tr><td><select name="os0">
					<option value="Android">Android $2,500.00 USD</option>
					<option value="iOS">iOS $2,500.00 USD</option>
					<option value="Windows Phone">Windows Phone $5,000.00 USD</option>
				</select></td></tr>
			</table>
			<input type="hidden" name="currency_code" value="USD">
			<input type="image" src="https://www.paypalobjects.com/en_US/i/btn/btn_buynowCC_LG.gif" border="0" name="submit" alt="PayPal - The safer, easier way to pay online!">
			<img alt="" border="0" src="https://www.paypalobjects.com/en_US/i/scr/pixel.gif" width="1" height="1">
		</form>
	</div>
</div>
""")

print('<script src="/assets/js/circuit-background-script.js" type="text/javascript"></script>')

with open("templates/footer.html", "r") as footer:
	print footer.read()




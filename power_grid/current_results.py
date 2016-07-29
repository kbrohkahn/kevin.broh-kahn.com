#!/usr/bin/env python
with open("../templates/header.html", "r") as header:
	print header.read()
with open("../templates/navbar.html", "r") as navbar:
	print navbar.read()
with open("results_header.html", "r") as resultsHeader:
	print resultsHeader.read()

header = ("Badge", "Full Name", "H1?", "H2?", "H3?", "P1", "P2", "P3", "W in 1st", "W in 2nd", "W in 3rd", "Total Points", "Attendance missing from table.")

print """
<h4>2016 results (All 3 heats)</h4>
<h2>All 30 winners advance to semis!</h2>
<b>Alternates will advance if less than 25 winners show up for semis. If you are a top 5 alternate, you might want to show up to the semis Saturday at 1100 in Ballroom.</b>
<br>
<br>
<br>
<br>
<div class="winner">Winner, guaranteed advance</div>
<div class="alternate-high">High alternate, please show up to SF</div>
<div class="alternate-low">Low alternate</div>
<br>
<div class="scroll-x">
	<table class="table">
		<thead>
			<tr>
				<th>Place</th>
				<th>Badge</th>
				<th>Full Name</th>
				<th>Heat 1<br>Entry?</th>
				<th>Heat 2<br>Entry?</th>
				<th>Heat 3<br>Entry?</th>
				<th>Heat 1<br>Points</th>
				<th>Heat 2<br>Points</th>
				<th>Heat 3<br>Points</th>
				<th>Win in 1st entry?</th>
				<th>Win in 2nd entry?</th>
				<th>Win in 3rd entry?</th>
				<th>Total Points</th>
			</tr>
		</thead>
		<tbody>
"""

results = (("1", "56", "Rick Atwater", "TRUE", "TRUE", "TRUE", "10", "10", "4", "TRUE", "TRUE", "FALSE", "24", "TRUE"),
("2", "5205", "Cody Zimmerman", "TRUE", "TRUE", "FALSE", "10", "10", "0", "TRUE", "TRUE", "FALSE", "20", "TRUE"),
("3", "1205", "Jason A. Ley", "TRUE", "TRUE", "TRUE", "10", "1", "10", "TRUE", "FALSE", "TRUE", "21", "TRUE"),
("4", "5621", "Carl Shapiro", "TRUE", "FALSE", "TRUE", "10", "0", "4", "TRUE", "FALSE", "FALSE", "14", "TRUE"),
("5", "5621", "Carl Shapiro", "TRUE", "FALSE", "TRUE", "10", "0", "4", "TRUE", "FALSE", "FALSE", "14", "TRUE"),
("6", "301", "Jim Savarick", "TRUE", "TRUE", "FALSE", "10", "4", "0", "TRUE", "FALSE", "FALSE", "14", "TRUE"),
("7", "600", "Woolly Farrow V", "TRUE", "TRUE", "FALSE", "10", "4", "0", "TRUE", "FALSE", "FALSE", "14", "TRUE"),
("8", "4984", "Chris Erickson", "TRUE", "TRUE", "TRUE", "10", "1", "2", "TRUE", "FALSE", "FALSE", "13", "TRUE"),
("9", "7065", "Peter Nystrom", "TRUE", "FALSE", "TRUE", "10", "0", "2", "TRUE", "FALSE", "FALSE", "12", "TRUE"),
("10", "3788", "Craig Trader", "TRUE", "TRUE", "FALSE", "10", "2", "0", "TRUE", "FALSE", "FALSE", "12", "TRUE"),
("11", "5101", "Kristina Lynch", "TRUE", "TRUE", "TRUE", "10", "0", "0", "TRUE", "FALSE", "FALSE", "10", "TRUE"),
("12", "433", "Rodney Davidson", "TRUE", "FALSE", "TRUE", "10", "0", "0", "TRUE", "FALSE", "FALSE", "10", "TRUE"),
("13", "1099", "Steve Koleszar", "FALSE", "FALSE", "TRUE", "0", "0", "10", "TRUE", "FALSE", "FALSE", "10", "TRUE"),
("14", "4196", "Peter Eldridge", "FALSE", "FALSE", "TRUE", "0", "0", "10", "TRUE", "FALSE", "FALSE", "10", "TRUE"),
("15", "3839", "Romain Jacques", "FALSE", "FALSE", "TRUE", "0", "0", "10", "TRUE", "FALSE", "FALSE", "10", "TRUE"),
("16", "6701", "Anthony Bosca", "FALSE", "TRUE", "FALSE", "0", "10", "0", "TRUE", "FALSE", "FALSE", "10", "TRUE"),
("17", "6993", "Kara Morse", "FALSE", "TRUE", "FALSE", "0", "10", "0", "TRUE", "FALSE", "FALSE", "10", "TRUE"),
("18", "1172", "Roderick Lee", "TRUE", "FALSE", "FALSE", "10", "0", "0", "TRUE", "FALSE", "FALSE", "10", "TRUE"),
("19", "1533", "Sam Packwood", "TRUE", "FALSE", "FALSE", "10", "0", "0", "TRUE", "FALSE", "FALSE", "10", "TRUE"),
("20", "4829", "Steven LeWinter", "TRUE", "FALSE", "FALSE", "10", "0", "0", "TRUE", "FALSE", "FALSE", "10", "TRUE"),
("21", "6027", "Kevin Burns", "TRUE", "FALSE", "FALSE", "10", "0", "0", "TRUE", "FALSE", "FALSE", "10", "TRUE"),
("22", "6897", "Peter Martinson", "FALSE", "FALSE", "FALSE", "0", "0", "10", "TRUE", "FALSE", "FALSE", "10", "TRUE"),
("23", "7164", "Moon Sultana", "TRUE", "TRUE", "TRUE", "4", "10", "4", "FALSE", "TRUE", "FALSE", "18", "TRUE"),
("24", "4289", "Tim Horne", "TRUE", "TRUE", "FALSE", "4", "10", "0", "FALSE", "TRUE", "FALSE", "14", "TRUE"),
("25", "6866", "David Borton", "TRUE", "TRUE", "FALSE", "4", "10", "0", "FALSE", "TRUE", "FALSE", "14", "TRUE"),
("26", "1852", "Philip Shea", "TRUE", "TRUE", "FALSE", "0", "10", "0", "FALSE", "TRUE", "FALSE", "10", "TRUE"),
("27", "3082", "Brad Sherwood", "TRUE", "FALSE", "TRUE", "4", "0", "10", "FALSE", "FALSE", "FALSE", "14", "TRUE"),
("28", "2748", "Kevin Broh-Kahn", "TRUE", "FALSE", "FALSE", "4", "0", "10", "FALSE", "FALSE", "FALSE", "14", "TRUE"),
("29", "4513", "Eugene Hourany", "TRUE", "FALSE", "TRUE", "2", "0", "10", "FALSE", "FALSE", "FALSE", "12", "TRUE"),
("30", "5204", "Dave Blisard", "TRUE", "FALSE", "TRUE", "2", "0", "10", "FALSE", "FALSE", "FALSE", "12", "TRUE"),
("31", "196", "Michael Brazinski", "TRUE", "TRUE", "TRUE", "4", "4", "1", "FALSE", "FALSE", "FALSE", "9", "TRUE"),
("32", "7067", "Lars Mattsson", "TRUE", "TRUE", "TRUE", "4", "0", "2", "FALSE", "FALSE", "FALSE", "6", "TRUE"),
("33", "1199", "Keith Levy", "TRUE", "FALSE", "TRUE", "4", "0", "2", "FALSE", "FALSE", "FALSE", "6", "TRUE"),
("34", "971", "John Jacoby", "TRUE", "FALSE", "TRUE", "2", "0", "4", "FALSE", "FALSE", "FALSE", "6", "TRUE"),
("35", "5614", "Quang Huynh", "TRUE", "FALSE", "TRUE", "2", "0", "4", "FALSE", "FALSE", "FALSE", "6", "TRUE"),
("36", "5331", "Tim Carnahan", "TRUE", "TRUE", "FALSE", "4", "2", "0", "FALSE", "FALSE", "FALSE", "6", "TRUE"),
("37", "3718", "Alyssa Mills", "TRUE", "TRUE", "TRUE", "0", "1", "4", "FALSE", "FALSE", "FALSE", "5", "TRUE"),
("38", "6482", "Pieter Villon", "TRUE", "TRUE", "TRUE", "2", "2", "1", "FALSE", "FALSE", "FALSE", "5", "TRUE"),
("39", "6798", "Jay Spencer", "TRUE", "TRUE", "TRUE", "0", "4", "0", "FALSE", "FALSE", "FALSE", "4", "TRUE"),
("40", "6483", "Jean Villon", "TRUE", "TRUE", "TRUE", "0", "2", "2", "FALSE", "FALSE", "FALSE", "4", "TRUE"),
("41", "1198", "Jason Levine", "FALSE", "TRUE", "TRUE", "0", "4", "0", "FALSE", "FALSE", "FALSE", "4", "TRUE"),
("42", "1733", "Greg Romano", "TRUE", "FALSE", "TRUE", "0", "0", "4", "FALSE", "FALSE", "FALSE", "4", "TRUE"),
("43", "3842", "Glen Pearce", "FALSE", "FALSE", "TRUE", "0", "0", "4", "FALSE", "FALSE", "FALSE", "4", "TRUE"),
("44", "7236", "James Marshall", "FALSE", "FALSE", "TRUE", "0", "0", "4", "FALSE", "FALSE", "FALSE", "4", "TRUE"),
("45", "2114", "Thomas Vickery", "TRUE", "TRUE", "FALSE", "0", "4", "0", "FALSE", "FALSE", "FALSE", "4", "TRUE"),
("46", "6396", "Pete Noteman", "FALSE", "TRUE", "FALSE", "0", "4", "0", "FALSE", "FALSE", "FALSE", "4", "TRUE"),
("47", "6992", "Frank Dinoff", "FALSE", "TRUE", "FALSE", "0", "4", "0", "FALSE", "FALSE", "FALSE", "4", "TRUE"),
("48", "1224", "Larry Loiacono", "TRUE", "FALSE", "FALSE", "4", "0", "0", "FALSE", "FALSE", "FALSE", "4", "TRUE"),
("49", "1374", "David Metzger", "TRUE", "FALSE", "FALSE", "4", "0", "0", "FALSE", "FALSE", "FALSE", "4", "TRUE"),
("50", "1419", "Lyman Moquin", "TRUE", "FALSE", "FALSE", "4", "0", "0", "FALSE", "FALSE", "FALSE", "4", "TRUE"),
("51", "4159", "Paul Sampson", "TRUE", "FALSE", "FALSE", "4", "0", "0", "FALSE", "FALSE", "FALSE", "4", "TRUE"),
("52", "4649", "Nessa Savarick", "TRUE", "FALSE", "FALSE", "4", "0", "0", "FALSE", "FALSE", "FALSE", "4", "TRUE"),
("53", "7156", "Devin Smith", "TRUE", "FALSE", "FALSE", "4", "0", "0", "FALSE", "FALSE", "FALSE", "4", "TRUE"),
("54", "691", "Jim Fry", "FALSE", "TRUE", "TRUE", "0", "2", "1", "FALSE", "FALSE", "FALSE", "3", "TRUE"),
("55", "718", "Pete Gathmann", "FALSE", "FALSE", "TRUE", "0", "1", "2", "FALSE", "FALSE", "FALSE", "3", "TRUE"),
("56", "4151", "Lexi Shea", "TRUE", "FALSE", "TRUE", "0", "0", "2", "FALSE", "FALSE", "FALSE", "2", "TRUE"),
("57", "4869", "Deb Yaure", "FALSE", "FALSE", "TRUE", "0", "0", "2", "FALSE", "FALSE", "FALSE", "2", "TRUE"),
("58", "6564", " Greg Stanton", "FALSE", "FALSE", "TRUE", "0", "0", "2", "FALSE", "FALSE", "FALSE", "2", "TRUE"),
("59", "599", "Daniel Farrow IV", "TRUE", "TRUE", "FALSE", "0", "2", "0", "FALSE", "FALSE", "FALSE", "2", "TRUE"),
("60", "5824", "Todd Trahan", "TRUE", "TRUE", "FALSE", "0", "2", "0", "FALSE", "FALSE", "FALSE", "2", "TRUE"),
("61", "6339", "Ashley Zimmerman", "TRUE", "TRUE", "FALSE", "2", "0", "0", "FALSE", "FALSE", "FALSE", "2", "TRUE"),
("62", "1602", "David Platnick", "FALSE", "TRUE", "FALSE", "0", "2", "0", "FALSE", "FALSE", "FALSE", "2", "TRUE"),
("63", "271", "Matt Calkins", "TRUE", "FALSE", "FALSE", "2", "0", "0", "FALSE", "FALSE", "FALSE", "2", "TRUE"),
("64", "3822", "Peggy Pfeifer", "TRUE", "FALSE", "FALSE", "2", "0", "0", "FALSE", "FALSE", "FALSE", "2", "TRUE"),
("65", "6021", "Joe Milloch", "TRUE", "FALSE", "FALSE", "2", "0", "0", "FALSE", "FALSE", "FALSE", "2", "TRUE"),
("66", "6125", "Colin Laird", "TRUE", "FALSE", "FALSE", "2", "0", "0", "FALSE", "FALSE", "FALSE", "2", "TRUE"),
("67", "6986", "Brian Hixon", "TRUE", "FALSE", "FALSE", "2", "0", "0", "FALSE", "FALSE", "FALSE", "2", "TRUE"),
("68", "7139", "Nicole White", "TRUE", "FALSE", "FALSE", "2", "0", "0", "FALSE", "FALSE", "FALSE", "2", "TRUE"),
("69", "4388", "Aidan Czyryca", "FALSE", "TRUE", "TRUE", "0", "0", "1", "FALSE", "FALSE", "FALSE", "1", "TRUE"),
("70", "885", "Harald Henning", "FALSE", "FALSE", "TRUE", "0", "0", "1", "FALSE", "FALSE", "FALSE", "1", "TRUE"),
("71", "4527", "Kelly Krieble", "FALSE", "FALSE", "TRUE", "0", "0", "1", "FALSE", "FALSE", "FALSE", "1", "TRUE"),
("72", "113", "Barrington Beavis", "FALSE", "FALSE", "TRUE", "0", "0", "1", "FALSE", "FALSE", "FALSE", "1", "TRUE"),
("73", "150", "Jeff Billings", "TRUE", "TRUE", "FALSE", "0", "1", "0", "FALSE", "FALSE", "FALSE", "1", "TRUE"),
("74", "1254", "Skip Maloney", "FALSE", "TRUE", "FALSE", "0", "1", "0", "FALSE", "FALSE", "FALSE", "1", "TRUE"),
("75", "6637", "Ricky Boyes", "FALSE", "TRUE", "FALSE", "0", "1", "0", "FALSE", "FALSE", "FALSE", "1", "TRUE"),
("76", "6760", "Chris Morse", "FALSE", "TRUE", "FALSE", "0", "1", "0", "FALSE", "FALSE", "FALSE", "1", "TRUE"),
("77", "2880", "Ernest Czyryca", "FALSE", "TRUE", "FALSE", "0", "0", "1", "FALSE", "FALSE", "FALSE", "1", "TRUE"),
("78", "5689", "Patrick Murphy", "TRUE", "FALSE", "FALSE", "1", "0", "0", "FALSE", "FALSE", "FALSE", "1", "TRUE"),
("79", "6741", "Dan Harthan", "TRUE", "FALSE", "FALSE", "1", "0", "0", "FALSE", "FALSE", "FALSE", "1", "TRUE"),
("80", "2881", "Kelly Czyryca", "FALSE", "FALSE", "FALSE", "0", "0", "1", "FALSE", "FALSE", "FALSE", "1", "TRUE"),
("81", "7123", "Eric McGlohon", "FALSE", "TRUE", "TRUE", "0", "0", "0", "FALSE", "FALSE", "FALSE", "0", "TRUE"),
("82", "3794", "Bertha Torres-Harris", "TRUE", "FALSE", "TRUE", "0", "0", "0", "FALSE", "FALSE", "FALSE", "0", "TRUE"),
("83", "4223", "Eric Harthan", "TRUE", "FALSE", "TRUE", "0", "0", "0", "FALSE", "FALSE", "FALSE", "0", "TRUE"),
("84", "1727", "David Rohde", "FALSE", "FALSE", "TRUE", "0", "0", "0", "FALSE", "FALSE", "FALSE", "0", "TRUE"),
("85", "3090", "Chris Czyryca", "FALSE", "FALSE", "TRUE", "0", "0", "0", "FALSE", "FALSE", "FALSE", "0", "TRUE"),
("86", "7133", "John Powers", "FALSE", "FALSE", "TRUE", "0", "0", "0", "FALSE", "FALSE", "FALSE", "0", "TRUE"),
("87", "4806", "Thomas Idzikowski", "FALSE", "FALSE", "TRUE", "0", "0", "0", "FALSE", "FALSE", "FALSE", "0", "TRUE"),
("88", "5678", "Bob Mazzi", "TRUE", "TRUE", "FALSE", "0", "0", "0", "FALSE", "FALSE", "FALSE", "0", "TRUE"),
("89", "3815", "Michael Shea", "FALSE", "TRUE", "FALSE", "0", "0", "0", "FALSE", "FALSE", "FALSE", "0", "TRUE"),
("90", "350", "Rolinda Collinson", "TRUE", "FALSE", "FALSE", "0", "0", "0", "FALSE", "FALSE", "FALSE", "0", "TRUE"),
("91", "862", "Franklin Haskell", "TRUE", "FALSE", "FALSE", "0", "0", "0", "FALSE", "FALSE", "FALSE", "0", "TRUE"),
("92", "2016", "Jamie Tang", "TRUE", "FALSE", "FALSE", "0", "0", "0", "FALSE", "FALSE", "FALSE", "0", "TRUE"),
("93", "3054", "Carol Haney", "TRUE", "FALSE", "FALSE", "0", "0", "0", "FALSE", "FALSE", "FALSE", "0", "TRUE"),
("94", "3432", "Eric Engelmann", "TRUE", "FALSE", "FALSE", "0", "0", "0", "FALSE", "FALSE", "FALSE", "0", "TRUE"),
("95", "3462", "Wesley Mauder", "TRUE", "FALSE", "FALSE", "0", "0", "0", "FALSE", "FALSE", "FALSE", "0", "TRUE"),
("96", "5726", "Chris Kalmbacher", "TRUE", "FALSE", "FALSE", "0", "0", "0", "FALSE", "FALSE", "FALSE", "0", "TRUE"),
("97", "6503", "Christopher Cameron", "TRUE", "FALSE", "FALSE", "0", "0", "0", "FALSE", "FALSE", "FALSE", "0", "TRUE"),
("98", "6644", "Alfred Schnabel", "TRUE", "FALSE", "FALSE", "0", "0", "0", "FALSE", "FALSE", "FALSE", "0", "TRUE"),
("99", "6799", "Matt  Spencer", "TRUE", "FALSE", "FALSE", "0", "0", "0", "FALSE", "FALSE", "FALSE", "0", "TRUE"),
("100", "7082", "Cyril Tircuit", "TRUE", "FALSE", "FALSE", "0", "0", "0", "FALSE", "FALSE", "FALSE", "0", "TRUE"),
("101", "7083", "Anastasia Tircuit", "TRUE", "FALSE", "FALSE", "0", "0", "0", "FALSE", "FALSE", "FALSE", "0", "TRUE"),
("102", "7149", "Berney Pellet", "TRUE", "FALSE", "FALSE", "0", "0", "0", "FALSE", "FALSE", "FALSE", "0", "TRUE"),
("103", "7197", "Hennessy Gorham", "TRUE", "FALSE", "FALSE", "0", "0", "0", "FALSE", "FALSE", "FALSE", "0", "TRUE"),
("104", "7198", "Tyson Henning", "TRUE", "FALSE", "FALSE", "0", "0", "0", "FALSE", "FALSE", "FALSE", "0", "TRUE"))

lastWinnerIndex = 99
numAlternates = 5

print ""
for i in range(0, len(results)):
	result = results[i]
	isWinner = int(result[12]) >= 10
	if lastWinnerIndex == 99 and not isWinner:
		lastWinnerIndex = i - 1

	classString = ""
	if isWinner:
		classString=" class='winner'"
	elif i > lastWinnerIndex and i <= lastWinnerIndex + numAlternates:
		classString=" class='alternate-high'"
	else:
		classString=" class='alternate-low'"

	print("<tr{0}>".format(classString))

	for value in result:
		print("<td>{0}</td>".format(value))
	print("</tr>")

print("</tbody></table></div>")

with open("../templates/footer.html", "r") as footer:
	print footer.read()

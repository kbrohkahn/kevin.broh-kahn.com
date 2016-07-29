#!/usr/bin/env python
with open("../templates/header.html", "r") as header:
	print header.read()
with open("../templates/navbar.html", "r") as navbar:
	print navbar.read()
with open("results_header.html", "r") as resultsHeader:
	print resultsHeader.read()

header = ("Badge", "Full Name", "H1?", "H2?", "H3?", "P1", "P2", "P3", "W in 1st", "W in 2nd", "W in 3rd", "Total Points", "Attendance missing from table.")

print """
<h4>2016 results (through 2 heats)</h4>
<h2>All 30 winners advance to semis!</h2>
<b>Alternates will advance if less than 25 winners show up for semis. If you are a top 5 alternate, you might want to show up to the semis Saturday at 1100 in Ballroom.</b>
<div class="winner">Winner, guaranteed advance</div>
<div class="alternate-high">High alternate, please show up to SF</div>
<div class="alternate-low">Low alternate</div>
<div class="scroll-x">
	<table class="table table-striped">
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

results = (("1", "5205", "Cody Zimmerman", "TRUE", "TRUE", "FALSE", "10", "10", "0", "TRUE", "TRUE", "FALSE", "20"),
("2", "56", "Rick Atwater", "TRUE", "TRUE", "FALSE", "10", "10", "0", "TRUE", "TRUE", "FALSE", "20"),
("3", "301", "Jim Savarick", "TRUE", "TRUE", "FALSE", "10", "4", "0", "TRUE", "FALSE", "FALSE", "14"),
("4", "600", "Woolly Farrow V", "TRUE", "TRUE", "FALSE", "10", "4", "0", "TRUE", "FALSE", "FALSE", "14"),
("5", "3788", "Craig Trader", "TRUE", "TRUE", "FALSE", "10", "2", "0", "TRUE", "FALSE", "FALSE", "12"),
("6", "1205", "Jason A. Ley", "TRUE", "TRUE", "FALSE", "10", "1", "0", "TRUE", "FALSE", "FALSE", "11"),
("7", "4984", "Chris Erickson", "TRUE", "TRUE", "FALSE", "10", "1", "0", "TRUE", "FALSE", "FALSE", "11"),
("8", "5101", "Kristina Lynch", "TRUE", "TRUE", "FALSE", "10", "0", "0", "TRUE", "FALSE", "FALSE", "10"),
("9", "433", "Rodney Davidson", "TRUE", "FALSE", "FALSE", "10", "0", "0", "TRUE", "FALSE", "FALSE", "10"),
("10", "1172", "Roderick Lee", "TRUE", "FALSE", "FALSE", "10", "0", "0", "TRUE", "FALSE", "FALSE", "10"),
("11", "1533", "Sam Packwood", "TRUE", "FALSE", "FALSE", "10", "0", "0", "TRUE", "FALSE", "FALSE", "10"),
("12", "4829", "Steven LeWinter", "TRUE", "FALSE", "FALSE", "10", "0", "0", "TRUE", "FALSE", "FALSE", "10"),
("13", "5621", "Carl Shapiro", "TRUE", "FALSE", "FALSE", "10", "0", "0", "TRUE", "FALSE", "FALSE", "10"),
("14", "6027", "Kevin Burns", "TRUE", "FALSE", "FALSE", "10", "0", "0", "TRUE", "FALSE", "FALSE", "10"),
("15", "7065", "Peter Nystrom", "TRUE", "FALSE", "FALSE", "10", "0", "0", "TRUE", "FALSE", "FALSE", "10"),
("16", "6701", "Anthony Bosca", "FALSE", "TRUE", "FALSE", "0", "10", "0", "TRUE", "FALSE", "FALSE", "10"),
("17", "6993", "Kara Morse", "FALSE", "TRUE", "FALSE", "0", "10", "0", "TRUE", "FALSE", "FALSE", "10"),
("18", "4289", "Tim Horne", "TRUE", "TRUE", "FALSE", "4", "10", "0", "FALSE", "TRUE", "FALSE", "14"),
("19", "6866", "David Borton", "TRUE", "TRUE", "FALSE", "4", "10", "0", "FALSE", "TRUE", "FALSE", "14"),
("20", "7164", "Moon Sultana", "TRUE", "TRUE", "FALSE", "4", "10", "0", "FALSE", "TRUE", "FALSE", "14"),
("21", "1852", "Philip Shea", "TRUE", "TRUE", "FALSE", "0", "10", "0", "FALSE", "TRUE", "FALSE", "10"),
("22", "196", "Michael Brazinski", "TRUE", "TRUE", "FALSE", "4", "4", "0", "FALSE", "FALSE", "FALSE", "8"),
("23", "5331", "Tim Carnahan", "TRUE", "TRUE", "FALSE", "4", "2", "0", "FALSE", "FALSE", "FALSE", "6"),
("24", "2114", "Thomas Vickery", "TRUE", "TRUE", "FALSE", "0", "4", "0", "FALSE", "FALSE", "FALSE", "4"),
("25", "6482", "Pieter Villon", "TRUE", "TRUE", "FALSE", "2", "2", "0", "FALSE", "FALSE", "FALSE", "4"),
("26", "6798", "Jay Spencer", "TRUE", "TRUE", "FALSE", "0", "4", "0", "FALSE", "FALSE", "FALSE", "4"),
("27", "7067", "Lars Mattsson", "TRUE", "TRUE", "FALSE", "4", "0", "0", "FALSE", "FALSE", "FALSE", "4"),
("28", "1199", "Keith Levy", "TRUE", "FALSE", "FALSE", "4", "0", "0", "FALSE", "FALSE", "FALSE", "4"),
("29", "1224", "Larry Loiacono", "TRUE", "FALSE", "FALSE", "4", "0", "0", "FALSE", "FALSE", "FALSE", "4"),
("30", "1374", "David Metzger", "TRUE", "FALSE", "FALSE", "4", "0", "0", "FALSE", "FALSE", "FALSE", "4"),
("31", "1419", "Lyman Moquin", "TRUE", "FALSE", "FALSE", "4", "0", "0", "FALSE", "FALSE", "FALSE", "4"),
("32", "2748", "Kevin Broh-Kahn", "TRUE", "FALSE", "FALSE", "4", "0", "0", "FALSE", "FALSE", "FALSE", "4"),
("33", "3082", "Brad Sherwood", "TRUE", "FALSE", "FALSE", "4", "0", "0", "FALSE", "FALSE", "FALSE", "4"),
("34", "4159", "Paul Sampson", "TRUE", "FALSE", "FALSE", "4", "0", "0", "FALSE", "FALSE", "FALSE", "4"),
("35", "4649", "Nessa Savarick", "TRUE", "FALSE", "FALSE", "4", "0", "0", "FALSE", "FALSE", "FALSE", "4"),
("36", "7156", "Devin Smith", "TRUE", "FALSE", "FALSE", "4", "0", "0", "FALSE", "FALSE", "FALSE", "4"),
("37", "1198", "Jason Levine", "FALSE", "TRUE", "FALSE", "0", "4", "0", "FALSE", "FALSE", "FALSE", "4"),
("38", "6396", "Pete Noteman", "FALSE", "TRUE", "FALSE", "0", "4", "0", "FALSE", "FALSE", "FALSE", "4"),
("39", "6992", "Frank Dinoff", "FALSE", "TRUE", "FALSE", "0", "4", "0", "FALSE", "FALSE", "FALSE", "4"),
("40", "599", "Daniel Farrow IV", "TRUE", "TRUE", "FALSE", "0", "2", "0", "FALSE", "FALSE", "FALSE", "2"),
("41", "5824", "Todd Trahan", "TRUE", "TRUE", "FALSE", "0", "2", "0", "FALSE", "FALSE", "FALSE", "2"),
("42", "6339", "Ashley Zimmerman", "TRUE", "TRUE", "FALSE", "2", "0", "0", "FALSE", "FALSE", "FALSE", "2"),
("43", "6483", "Jean Villon", "TRUE", "TRUE", "FALSE", "0", "2", "0", "FALSE", "FALSE", "FALSE", "2"),
("44", "271", "Matt Calkins", "TRUE", "FALSE", "FALSE", "2", "0", "0", "FALSE", "FALSE", "FALSE", "2"),
("45", "971", "John Jacoby", "TRUE", "FALSE", "FALSE", "2", "0", "0", "FALSE", "FALSE", "FALSE", "2"),
("46", "3822", "Peggy Pfeifer", "TRUE", "FALSE", "FALSE", "2", "0", "0", "FALSE", "FALSE", "FALSE", "2"),
("47", "4513", "Eugene Hourany", "TRUE", "FALSE", "FALSE", "2", "0", "0", "FALSE", "FALSE", "FALSE", "2"),
("48", "5204", "Dave Blisard", "TRUE", "FALSE", "FALSE", "2", "0", "0", "FALSE", "FALSE", "FALSE", "2"),
("49", "5614", "Quang Huynh", "TRUE", "FALSE", "FALSE", "2", "0", "0", "FALSE", "FALSE", "FALSE", "2"),
("50", "6021", "Joe Milloch", "TRUE", "FALSE", "FALSE", "2", "0", "0", "FALSE", "FALSE", "FALSE", "2"),
("51", "6125", "Colin Laird", "TRUE", "FALSE", "FALSE", "2", "0", "0", "FALSE", "FALSE", "FALSE", "2"),
("52", "6986", "Brian Hixon", "TRUE", "FALSE", "FALSE", "2", "0", "0", "FALSE", "FALSE", "FALSE", "2"),
("53", "7139", "Nicole White", "TRUE", "FALSE", "FALSE", "2", "0", "0", "FALSE", "FALSE", "FALSE", "2"),
("54", "1602", "David Platnick", "FALSE", "TRUE", "FALSE", "0", "2", "0", "FALSE", "FALSE", "FALSE", "2"),
("55", "691", "Jim Fry", "FALSE", "TRUE", "FALSE", "0", "2", "0", "FALSE", "FALSE", "FALSE", "2"),
("56", "150", "Jeff Billings", "TRUE", "TRUE", "FALSE", "0", "1", "0", "FALSE", "FALSE", "FALSE", "1"),
("57", "3718", "Alyssa Mills", "TRUE", "TRUE", "FALSE", "0", "1", "0", "FALSE", "FALSE", "FALSE", "1"),
("58", "5689", "Patrick Murphy", "TRUE", "FALSE", "FALSE", "1", "0", "0", "FALSE", "FALSE", "FALSE", "1"),
("59", "6741", "Dan Harthan", "TRUE", "FALSE", "FALSE", "1", "0", "0", "FALSE", "FALSE", "FALSE", "1"),
("60", "1254", "Skip Maloney", "FALSE", "TRUE", "FALSE", "0", "1", "0", "FALSE", "FALSE", "FALSE", "1"),
("61", "6637", "Ricky Boyes", "FALSE", "TRUE", "FALSE", "0", "1", "0", "FALSE", "FALSE", "FALSE", "1"),
("62", "6760", "Chris Morse", "FALSE", "TRUE", "FALSE", "0", "1", "0", "FALSE", "FALSE", "FALSE", "1"),
("63", "718", "Pete Gathmann", "FALSE", "FALSE", "FALSE", "0", "1", "0", "FALSE", "FALSE", "FALSE", "1"),
("64", "5678", "Bob Mazzi", "TRUE", "TRUE", "FALSE", "0", "0", "0", "FALSE", "FALSE", "FALSE", "0"),
("65", "350", "Rolinda Collinson", "TRUE", "FALSE", "FALSE", "0", "0", "0", "FALSE", "FALSE", "FALSE", "0"),
("66", "862", "Franklin Haskell", "TRUE", "FALSE", "FALSE", "0", "0", "0", "FALSE", "FALSE", "FALSE", "0"),
("67", "1733", "Greg Romano", "TRUE", "FALSE", "FALSE", "0", "0", "0", "FALSE", "FALSE", "FALSE", "0"),
("68", "2016", "Jamie Tang", "TRUE", "FALSE", "FALSE", "0", "0", "0", "FALSE", "FALSE", "FALSE", "0"),
("69", "3054", "Carol Haney", "TRUE", "FALSE", "FALSE", "0", "0", "0", "FALSE", "FALSE", "FALSE", "0"),
("70", "3432", "Eric Engelmann", "TRUE", "FALSE", "FALSE", "0", "0", "0", "FALSE", "FALSE", "FALSE", "0"),
("71", "3462", "Wesley Mauder", "TRUE", "FALSE", "FALSE", "0", "0", "0", "FALSE", "FALSE", "FALSE", "0"),
("72", "3794", "Bertha Torres-Harris", "TRUE", "FALSE", "FALSE", "0", "0", "0", "FALSE", "FALSE", "FALSE", "0"),
("73", "3794", "Bertha Torres-Harris", "TRUE", "FALSE", "FALSE", "0", "0", "0", "FALSE", "FALSE", "FALSE", "0"),
("74", "4151", "Lexi Shea", "TRUE", "FALSE", "FALSE", "0", "0", "0", "FALSE", "FALSE", "FALSE", "0"),
("75", "4151", "Lexi Shea", "TRUE", "FALSE", "FALSE", "0", "0", "0", "FALSE", "FALSE", "FALSE", "0"),
("76", "4223", "Eric Harthan", "TRUE", "FALSE", "FALSE", "0", "0", "0", "FALSE", "FALSE", "FALSE", "0"),
("77", "5726", "Chris Kalmbacher", "TRUE", "FALSE", "FALSE", "0", "0", "0", "FALSE", "FALSE", "FALSE", "0"),
("78", "6503", "Christopher Cameron", "TRUE", "FALSE", "FALSE", "0", "0", "0", "FALSE", "FALSE", "FALSE", "0"),
("79", "6644", "Alfred Schnabel", "TRUE", "FALSE", "FALSE", "0", "0", "0", "FALSE", "FALSE", "FALSE", "0"),
("80", "6799", "Matt  Spencer", "TRUE", "FALSE", "FALSE", "0", "0", "0", "FALSE", "FALSE", "FALSE", "0"),
("81", "7082", "Cyril Tircuit", "TRUE", "FALSE", "FALSE", "0", "0", "0", "FALSE", "FALSE", "FALSE", "0"),
("82", "7083", "Anastasia Tircuit", "TRUE", "FALSE", "FALSE", "0", "0", "0", "FALSE", "FALSE", "FALSE", "0"),
("83", "7149", "Berney Pellet", "TRUE", "FALSE", "FALSE", "0", "0", "0", "FALSE", "FALSE", "FALSE", "0"),
("84", "7197", "Hennessy Gorham", "TRUE", "FALSE", "FALSE", "0", "0", "0", "FALSE", "FALSE", "FALSE", "0"),
("85", "7198", "Tyson Henning", "TRUE", "FALSE", "FALSE", "0", "0", "0", "FALSE", "FALSE", "FALSE", "0"),
("86", "2880", "Ernest Czyryca", "FALSE", "TRUE", "FALSE", "0", "0", "0", "FALSE", "FALSE", "FALSE", "0"),
("87", "3815", "Michael Shea", "FALSE", "TRUE", "FALSE", "0", "0", "0", "FALSE", "FALSE", "FALSE", "0"),
("88", "4388", "Aidan Czyryca", "FALSE", "TRUE", "FALSE", "0", "0", "0", "FALSE", "FALSE", "FALSE", "0"),
("89", "7123", "Eric McGlohon", "FALSE", "TRUE", "FALSE", "0", "0", "0", "FALSE", "FALSE", "FALSE", "0"))

lastWinnerIndex = 99
numAlternates = 5

print ""
for i in range(0, len(results):
	result = results[i]
	isWinner = result[12] < 10
	if lastWinnerIndex == 99 and isWinner:
		lastWinnerIndex = i

	classString = ""
	if isWinner:
		classString=" class='winner'"
	elif i > lastWinnerIndex && i <= lastWinnerIndex + numAlternates:
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

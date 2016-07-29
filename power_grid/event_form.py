#!/usr/bin/env python
with open("../../templates/header.html", "r") as header:
	print header.read()
with open("../../templates/navbar.html", "r") as navbar:
	print navbar.read()

print("""
<div class="row">
	<div class="col-xs-12">		
		<select class="form-control" name="heat-number">
			<option>1</option>
			<option>2</option>
			<option>3</option>
		</select>
	</div>
	<div class="col-xs-12">
		<label>First<label>
		<input name="1-place-badge" class="form-control">
		<input name="1-place-name" class="form-control">
	</div>
	<div class="col-xs-12">
		<label>Second<label>
		<input name="2-place-badge" class="form-control">
		<input name="2-place-name" class="form-control">
	</div>
	<div class="col-xs-12">
		<label>Third<label>
		<input name="3-place-badge" class="form-control">
		<input name="3-place-name" class="form-control">
	</div>
	<div class="col-xs-12">
		<label>Fourth<label>
		<input name="4-place-badge" class="form-control">
		<input name="4-place-name" class="form-control">
	</div>
	<div class="col-xs-12">
		<label>Fifth<label>
		<input name="5-place-badge" class="form-control">
		<input name="5-place-name" class="form-control">
	</div>
</div>
""")


with open("../../templates/footer.html", "r") as footer:
	print footer.read()


try:
	form = cgi.FieldStorage()

	firstPlaceBadge = form.getvalue("1-place-badge", "")
	if firstPlaceBadge != "":
		nameTableValues = []
		resultTableValues = []
		
		for i in range(1, 5):
			nameTableValues	.append([form.getvalue(string(i) + "-place-badge"), form.getvalue(string(i) + "-place-name")])
			resultTableValues	.append([form.getvalue(string(i) + "-place-badge"), i])

			connection = sqlite3.connect('power_grid.db')
			cursor = connection.cursor()

			cursor.execute("insert into Names values(?, ?);", nameTableValues)
			cursor.execute("insert into Results_Heat_{0} values(?, ?)".format(form.getvalue("heat-number", "-1"), resultsTableValues)
		
			
			
						cursor.execute("INSERT INTO Recipes VALUES(?, ?, ?, ?);", (recipeId, recipe["name"], recipe["servings"], recipe["calories"]))

				





		clearForm()

		

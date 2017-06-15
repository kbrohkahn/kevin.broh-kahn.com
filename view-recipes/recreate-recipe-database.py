#!/usr/bin/env python
import json
import sqlite3

#
# recreate SQLite database from JSON file
#
allRecipes = []
with open("recipes.json") as jsonFile:
	for line in jsonFile:
		allRecipes.append(simplejson.loads(line))

try:
	# open database and get cursor
	connection = sqlite3.connect('recipes.db')
	cursor = connection.cursor()

	cursor.executescript("""
DROP TABLE IF EXISTS Recipes;
CREATE TABLE Recipes(Id INT, Name TEXT, Servings INT, Calories INT);

DROP TABLE IF EXISTS Directions;
CREATE TABLE Directions(RecipeId INT, Step INT, Direction TEXT);

DROP TABLE IF EXISTS Footnotes;
CREATE TABLE Footnotes(RecipeId INT, Footnote TEXT);

DROP TABLE IF EXISTS Labels;
CREATE TABLE Labels(RecipeId INT, Label TEXT);

DROP TABLE IF EXISTS Ingredients;
CREATE TABLE Ingredients(Id INT, RecipeId INT, Name TEXT, Amount INT, Unit TEXT);

DROP TABLE IF EXISTS IngredientDescriptions;
CREATE TABLE IngredientDescriptions(IngredientId INT, Description TEXT);

DROP TABLE IF EXISTS IngredientLabels;
CREATE TABLE IngredientLabels(IngredientId INT, Label TEXT);""")

	for recipe in allRecipes:
		recipeId = recipe["id"]
		cursor.execute("INSERT INTO Recipes VALUES(?, ?, ?, ?);", (recipeId, recipe["name"], recipe["servings"], recipe["calories"]))

		for direction in recipe["directions"]:
			cursor.execute("INSERT INTO Directions VALUES(?, ?, ?);", (recipeId, direction["step"], direction["direction"]))

		for footnote in recipe["footnotes"]:
			cursor.execute("INSERT INTO Footnotes VALUES(?, ?);", (recipeId, footnote))

		for label in recipe["labels"]:
			cursor.execute("INSERT INTO Labels VALUES(?, ?);", (recipeId, label))

		i=0
		for ingredient in recipe["ingredients"]:
			ingredientId = recipeId * 100 + i
			cursor.execute("INSERT INTO Ingredients VALUES(?, ?, ?, ?, ?);", (ingredientId, recipeId, ingredient["ingredient"], ingredient["amount"], ingredient["unit"]))

			for ingredientDescription in ingredient["descriptions"]:
				cursor.execute("INSERT INTO IngredientDescriptions VALUES(?, ?);", (ingredientId, ingredientDescription))

			for ingredientLabel in ingredient["labels"]:
				cursor.execute("INSERT INTO IngredientLabels VALUES(?, ?);", (ingredientId, ingredientLabel))

			i+=1

	# commit and close connection		
	connection.commit()
	connection.close()

# sqlite error
except sqlite3.Error as e:
	print("Error %s:" % e.args[0])

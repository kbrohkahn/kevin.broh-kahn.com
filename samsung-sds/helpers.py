#!/usr/bin/env python
import MySQLdb

def getDataFromSql(query):
	db = MySQLdb.connect(host="localhost",
	                     user="pi",
	                     passwd="#28cj2509",
	                     db="samsung_sds")
	cur = db.cursor()
	cur.execute(query)
	results = cur.fetchall()
	cur.close()
	db.close()



def printHeader(title):
	with open("templates/header.html", "r") as header:
		print header.read()
	print "<h1>" + title + "</h1>"



def printFooter():
	with open("templates/footer.html", "r") as footer:
		print navbar.read()



def printError(errorMessage):
	print "<b style='text-color: red'>" + errorMessage + "</b>"

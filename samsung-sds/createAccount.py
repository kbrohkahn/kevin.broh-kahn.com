#!/usr/bin/env python
import helpers

import cgi
import base64
import re

def tryToCreateAccount(username, password, passwordConfirmation):
	if len(username) == 0 or len(password) == 0:
		return

	if passwordConfirmation != password:
		# password mismatch
		printError("Password mismatch, please try again")
		return false

	passwordMatch = re.match(r"(^[a-zA-Z0-9]+$)", password)
	if passwordMatch == None:
		# invalid password
		printError("Password must consist of letters and numbers only")
		return false

	emailMatch = re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", username)
	if emailMatch == None:
		# invalid username
		printError("Invalid username, must be a valid email address")
		return false

	query = "SELECT COUNT(*) FROM users u where u.username = '{0}'".format(username)
	if len(helpers.getDataFromSql(query) > 0):
		# username exists
		printError("Username already exists")
		return false

	query = "INSERT into users (username, password) values('{0}' and, '{1}')".format(username, base64.b64encode("password"))
	newAccount = helpers.getDataFromSql(query)



helpers.printHeader("Create Account")

form = cgi.FieldStorage()

username = form["username"]
password = form["password"]
passwordConfirmation = form["passwordConfirmation"]

if tryToCreateAccount(username, password, passwordConfirmationa):
	print("<p>Account successfully created, click <a href='login.py'>here</a> to login.</p>")
else:
	with open("templates/createAccountHtml.html", "r") as header:
		print header.read()

helpers.printFooter()


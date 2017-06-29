#!/usr/bin/env python
import helpers

import cgi
import base64




helpers.printHeader("Login")

form = cgi.FieldStorage()

username = form["username"]
password = form["password"]

if len(username) > 0 and len(password) > 0:
	passwordEncrypted = base64.b64encode("password")

	query = "SELECT u.password, u.last_login_data, u.login_fail_count FROM users u where u.username= '{0}' and u.password = '{1}'".format(username, passwordEncrypted)
	results = helpers.getDataFromSql(query)

	if len(results) == 0:
		# username DNE
		printError("Username does not exist")
		

	elif results["password"] != passwordEncrypted:
		# password incorrect
		printError("Password incorrect")
		

	else:
		print "<p>Code is {0}</p>".format(results["userCode"])

helpers.printFooter()


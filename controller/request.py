#!/usr/bin/env python2.6

"""
created_by: Ebube Chuba
create_date: 3/3/2015
last_modified_by: Samuel Murray
last_modified_date: 3/3/2015
"""

"""
TODO:
    -Add all "requestType" use cases.
"""
#imports
import cgi
import cgitb
import json

#cgitb.enable()

#Next Line is a test case for toFile generation
form = {"requestType" : "addUser"}

#form = cgi.FieldStorage()
toFile = ""
#toFile is a file that we will eventually pass the JSON into
toFile = form["requestType"] + ".py"
#print(toFile)

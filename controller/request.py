#!/usr/bin/env python3

"""
created_by: Ebube Chuba
create_date: 3/3/2015
last_modified_by: Samuel Murray
last_modified_date: 3/4/2015
"""

"""
TODO:
    -Add all "requestType" use cases.
"""
#imports
import cgi
import cgitb
import json
import viewTopic
import constants

#cgitb.enable()

#Next Line is a test case for toFile generation
form = {"requestType" : "viewTopic", "id" : "all"}

#form = cgi.FieldStorage()
toFile = ""
#toFile is a file that we will eventually pass the JSON into
toFile = form["requestType"]
if constants.DEBUG > 0:
    print(toFile)
# viewTopic request handling
if toFile == "viewTopic":
    if form["id"] != "all":
        if len(form["id"] > 1):
            topicList = form["id"]
            for topic in topicList:
                print("Content-Type: text/html; charset=utf-8")
                print()
                print(viewTopic.byID(topic))
        else:
            print("Content-Type: text/html; charset=utf-8")
            print()
            print(viewTopic.byID(form["id"]))
    else:
        print("Content-Type: text/html; charset=utf-8")
        print()
        print(viewTopic.all())

#!/usr/locl/bin/python3

import cgi
import cgitb
import json
import sys
import constants

# if you find a better way to do this plz replace

cgitb.enable()

unprocessedForm = cgi.FieldStorage()

toFile = ""
#toFile is a file that we will eventually pass the JSON into
toFile = unprocessedForm["requestType"]
#if constants.DEBUG > 0:
#    print(toFile)

objectList = [ "User", "Assignment", "Section", "Course", "Topic", "Question"] #TODO add in all objects
verbList   = [ "add", "get", "update", "activate", "login" ]

# currVerb/Object can only come from the provided lists
# protects against injections
currVerb = ""
currObject = ""
for i in verbList:
    if i in toFile.value:
        currVerb = i

for i in objectList:
    if i in toFile.value:
        currObject = i

if currVerb == "login":
    # is login handled here?
    processedForm = "{success:failure}"
else:
    if currVerb != "" and currObject != "":
        verbObject = currVerb + currObject
        eval("import " + verbObject)
        processedForm = eval(verbObject + ".iChooseU(unprocessedForm)")
    else:
        # malformed tags go here?
        processedForm = "{success:failure}"

print("Content-Type: application/json; charset=utf-8")
print()
print(processedForm)

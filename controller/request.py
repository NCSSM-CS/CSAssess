#!/usr/locl/bin/python3

import cgi
import cgitb
import json
import sys
import constants

#=== Init ===#
cgitb.enable()

unprocessedForm = cgi.FieldStorage()

requestType = ""
requestType = unprocessedForm["requestType"]

objectList = [ "User", "Assignment", "Section", "Course", "Topic", "Question"] #TODO add in all objects
verbList   = [ "add", "get", "update", "activate", "login" ]
currVerb = ""
currObject = ""

#if constants.DEBUG > 0:
#    print(requestType)


#=== Body ===#
# currVerb/Object can only come from the provided lists
# protects against injections
# safe-ish
for i in verbList:
    if i in requestType.value:
        currVerb = i

for i in objectList:
    if i in requestType.value:
        currObject = i

if currVerb == "login":
    #TODO
    # is login handled in this file?
    processedForm = '{"success":"failure"}'
else:
    if currVerb != "" and currObject != "":
        verbObject = currVerb + currObject
        # this is supposed to be emulating "eval('import ' + verbObject)"
        #                   name      |  add to | add to | import [] from | level?
        module = __import__(verbObject, globals(), locals(), [], 0)
        processedForm = exec("module." + verbObject + ".iChooseU(unprocessedForm)")
    else:
        # malformed tags go here?
        #TODO
        processedForm = '{"success":"failure"}'

#=== Return JSON ===#
# format
print("Content-Type: application/json; charset=utf-8")
print()
# content
print(processedForm)

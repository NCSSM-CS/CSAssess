#!/usr/bin/local/python3

# Author : Caeman + Sam

import cgi
import cgitb
#import json
import sys
import constants

def processRequest(unprocessedForm):
    """ Receives cgi.FieldStorage() and returns JSON to be printed"""
    
    if "requestType" in unprocessedForm:
        requestType = unprocessedForm.getvalue("requestType")
        #return '{"success":"success?"}' # testing
        
    else:
        # received form contains no requestType
        return '{"success":"failure","mode":"noRequestType"}'


    objectList = [ "User", "Assignment", "Section", "Course", "Topic", "Question"] #TODO add in all objects
    verbList   = [ "add", "get", "update", "activate", "login" ]
    currVerb = ""
    currObject = ""
    
    # currVerb/Object can only come from the provided lists
    # protects against injections
    # safe-ish
    for i in verbList:
        if i in requestType:
            currVerb = i
    for i in objectList:
        if i in requestType:
            currObject = i
    
    if currVerb == "login":
        #TODO is login handled in this file?
        processedForm = '{"success":"failure","mode":"login"}'
    else:
        if currVerb != "" and currObject != "":
            verbObject = currVerb + currObject
            # this is supposed to be emulating "eval('import ' + verbObject)"
            module = __import__(verbObject)
            #TODO
            processedForm = exec("module." + verbObject + ".iChooseU(unprocessedForm)")
        else:
            #TODO malformed tags go here?
            processedForm = '{"success":"failure","mode":"malformed"}'

#=== Return JSON ===#
cgitb.enable()
unprocessedForm = cgi.FieldStorage()


print("Content-Type: application/json; charset=utf-8")
print()
print(processRequest(unprocessedForm))

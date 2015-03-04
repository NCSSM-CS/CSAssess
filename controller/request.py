#!/usr/bin/env python3

"""
created_by: Ebube Chuba
create_date: 3/3/2015
last_modified_by: Samuel Murray
last_modified_date: 3/4/2015
"""

#imports
import cgi
import cgitb
import json
import sys
import constants
#import addTopic
#import getTopic
#import updateTopic
#import activateTopic
#import getUser
#import addUser
#import updateUser
#import activateUser
#import getAssessment
#import addAssessment
#import updateAssessment
#import activateAssessment
import getQuestion
import addQuestion
#import updateQuestion
#import activateQuestion

cgitb.enable()

unprocessedForm = cgi.FieldStorage()
toFile = ""
#toFile is a file that we will eventually pass the JSON into
toFile = unprocessedForm["requestType"]
if constants.DEBUG > 0:
    print(toFile)
# Add Topic requestTypes
#if toFile == "getTopic":
#    processedForm = getTopic.iChooseU(unprocessedForm)
#elif toFile == "addTopic":
#    processedForm = addTopic.iChooseU(unprocessedForm)
#elif toFile == "updateTopic":
#    processedForm = updateTopic.iChooseU(unprocessedForm)
#elif toFile == "activateTopic":
#    processedForm = activateTopic.iChooseU(unprocessedForm)
# Add User requestTypes
#elif toFile == "getUser":
#    processedForm = getUser.iChooseUunprocessedForm)
#elif toFile == "addUser":
#    processedForm = addUser.iChooseU(unprocessedForm)
#elif toFile == "updateUser":
#    processedForm = updateUser.iChooseU(unprocessedForm)
#elif toFile == "activateUser":
#    processedForm = activateUser.iChooseU(unprocessedForm)
# Add Assessment requestTypes
#elif toFile == "getAssessment":
#    processedForm = getAssessment.iChooseU(unprocessedForm)
#elif toFile == "addAssessment":
#    processedForm = addAssessment.iCChooseU(unprocessedForm)
#elif toFile == "updateAssessment":
#    processedForm = updateAssessment.iChooseU(unprocessedForm)
#elif toFile == "activateAssignment":
#    processedForm = activateAssessment.iChooseU(unprocessedForm)
# Add Question requestTypes
elif toFile == "getQuestion":
    processedForm = getQuestion.iChooseU(unprocessedForm)
elif toFile == "addQuestion":
    processedForm = addQuestion.iChooseU(unprocessedForm)
#elif toFile == "updateQuestion":
#    processedForm = updateQuestion.iChooseU(unprocessedForm)
#elif toFile == "activateQuestion":
#    processedForm = activateQuestion.iChooseU(unprocessedForm)

print("Content-Type: application/json; charset=utf-8")
print()
print(processedForm)

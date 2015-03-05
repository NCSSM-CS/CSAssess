#!/usr/bin/env python3

"""
created_by: Ebube Chuba
create_date: 3/3/2015
last_modified_by: Ebube Chuba
last_modified_date: 3/5/2015
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
import getUser
import addUser
#import updateUser
#import activateUser
#import getAssessment
#import addAssessment
#import updateAssessment
#import activateAssessment
#import getQuestion
#import addQuestion
#import updateQuestion
#import activateQuestion
#import addAnswer
#import getAnswer
#import updateAnswer
#import activateAnswer
#import addCourse
#import getCourse
#import uppdateCourse
#import activateCourse
#import addSection
#import getSection
#import updateSection
#import activateSection

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
elif toFile == "getUser":
    processedForm = getUser.iChooseU(unprocessedForm)
elif toFile == "addUser":
    processedForm = addUser.iChooseU(unprocessedForm)
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
#elif toFile == "activateAssessment":
#    processedForm = activateAssessment.iChooseU(unprocessedForm)
# Add Question requestTypes
#elif toFile == "getQuestion":
#    processedForm = getQuestion.iChooseU(unprocessedForm)
#elif toFile == "addQuestion":
#    processedForm = addQuestion.iChooseU(unprocessedForm)
#elif toFile == "updateQuestion":
#    processedForm = updateQuestion.iChooseU(unprocessedForm)
#elif toFile == "activateQuestion":
#    processedForm = activateQuestion.iChooseU(unprocessedForm)
# Add Answer requestTypes
#elif toFile == "getAnswer":
#    processedForm = getAnswer.iChooseU(unprocessedForm)
#elif toFile == "addAnswer":
#    processedForm = addAnswer.iChooseU(unprocessedForm)
#elif toFile == "updateFile":
#    processedForm = updateAnswer.iChooseU(unprocessedForm)
#elif toFile == "activateAnswer"
#    processedForm = activateAnswer.iChooseU(unprocessedForm)
# Add Course requestTypes
#elif toFile == "getCourse":
#    processedForm = getCourse.iChooseU(unprocessedForm)
#elif toFile == "addCourse":
#    processedForm = addCourse.iChooseU(unprocessedForm)
#elif toFile == "updateCourse":
#    processedForm = updateCourse.iChooseU(unprocessedForm)
#elif toFile == "activateCourse":
#    processedForm = activateCourse.iChooseU(unprocessedForm)
# Add Section requestTypes
#elif toFile == "getSection":
#    processedForm = getSection.iChooseU(unprocessedForm)
#elif toFile == "addSection":
#    processedForm = addSection.iChooseU(unprocessedForm)
#elif toFile == "updateSection":
#    processedForm = updateSection.iChooseU(unprocessedForm)
#elif toFile == "activateSection":
#    processedForm = activateSection.iChooseU(unprocessedForm)

print("Content-Type: application/json; charset=utf-8")
print()
print(processedForm)

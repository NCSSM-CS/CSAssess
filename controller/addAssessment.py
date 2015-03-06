#!/usr/local/bin/python3

"""
created_by:         Aninda Manocha
created_date:       3/4/2015
last_modified_by:   Aninda Manocha
last_modified date: 3/6/2015
"""

# imports
import constants
import utils
import json
from sql.section import Section
from sql.session import Session
from sql.user import User
from sql.assessment import Assessment

#Format of assessment -AM
#requestType: assessment
#atype: "string" 
#section: "string"
#name: "string"
#questionList: []
#topicList: []

def iChooseU(form):
    thisUser = utils.findUser(form)

    atype = form["type"]
    section = Section.get(0, form["section"])[0]
    name = form["name"]
    questionList = form["questions"]
    topicList = form["topics"]
    
    listOfQuestions = []
    listOfTopics = []
    for q in questionList:
        listOfQuestions.append(Question.get(q)[0])
    for t in topicList:
        listOfTopics.append(Topic.get(t)[0])

    newAssessment = Assessment.noID(None, thisUser, atype, section, name, listOfQuestions, listOfTopics, 1)
    newAssessment.add()

    return utils.successJson(form)

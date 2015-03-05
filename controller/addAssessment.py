#!/usr/bin/python3

"""
created_by:         Aninda Manocha
created_date:       3/4/2015
last_modified_by:   Aninda Manocha
last_modified date: 3/4/2015
"""

# imports
import constants
import json
from sql.session import Session

#Format of assessment -AM
#requestType: assessment
#atype: "string" 
#section: section.id (Integer)
#name: "string"
#question_list: list of questions
#topic_list: list of topics

def iChooseU(json):
    thisUser = findUser()

    atype = json["type"]
    section = json["section"]
    name = json["name"]
    question_list = json["questions"]
    topic_list = json["topics"]

    newAssessment = Assessment.noID(None, thisUser, atype, section, name, question_list, topic_list, 1)
    newAssessment.add()

    successJson()

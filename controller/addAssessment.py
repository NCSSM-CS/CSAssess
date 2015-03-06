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
#question_list: list of questions
#topic_list: list of topics

def iChooseU(json):
    thisUser = utils.findUser(json)

    atype = json["type"]
    section = json["section"]
    thisSection = Section.get(0, section)[0]
    name = json["name"]
    question_list = json["questions"]
    topic_list = json["topics"]

    newAssessment = Assessment.noID(None, thisUser, atype, thisSection, name, question_list, topic_list, 1)
    newAssessment.add()

    return utils.successJson(json)

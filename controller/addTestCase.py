#!/usr/bin/python3

"""
created_by:         Aninda Manocha
created_date:       3/5/2015
last_modified_by:   Aninda Manocha
last_modified_date: 3/5/2015
"""

# imports
import constants
import utils
import json

#Format of test case -AM
#requestType: test case
#question: Question
#weight: integer
#content: "string"

def iChooseU(json):
    thisUser = findUser()

    question = json["question"]
    weight = json["weight"]
    content = json["content"]

    newTestCase = Test_Case.noID(None, thisUser, question, weight, content, ACTIVE)
    newTestCase.add()

    return successJson()

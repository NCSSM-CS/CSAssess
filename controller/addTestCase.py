#!/usr/local/bin/python3

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
from sql.question import Question
from sql.session import Session

#Format of test case -AM
#requestType: addTestCase
#question: Question
#weight: integer
#content: "string"

def iChooseU(json):
    thisUser = utils.findUser(json)

    question = json["question"]
    theQuestion = Question.get(question["id"])[0]
    weight = json["weight"]
    content = json["content"]

    newTestCase = Test_Case.noID(None, thisUser, theQuestion, weight, content, ACTIVE)
    newTestCase.add()

    return utils.successJson(json)

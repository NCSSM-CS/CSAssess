#!/usr/local/bin/python3

"""
created_by:         Aninda Manocha
created_date:       3/5/2015
last_modified_by:   Keshav Patel
last_modified_date: 3/6/2015
"""

# imports
import constants
import utils
import json
from sql.user import User
from sql.question import Question
from sql.session import Session
from sql.test_case import Test_Case

#Format of test case -AM
#requestType: addTestCase
#question: question id  integer
#weight:                integer
#content:               string

def iChooseU(form):
    thisUser = utils.findUser(form)

    question = form["question"]
    theQuestion = Question.get(question)[0]
    weight = form["weight"]
    content = form["content"]

    newTestCase = Test_Case.noID(None, thisUser, theQuestion, weight, content, ACTIVE)
    newTestCase.add()

    return utils.successJson(form)

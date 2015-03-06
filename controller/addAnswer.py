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
from sql.user import User
from sql.question import Question
from sql.answer import Answer
from sql.session import Session

#Format of answer -AM
#requestType: addAnswer
#question: integer
#content: "string"
#isSolution: boolean

def iChooseU(json):
    thisUser = utils.findUser(json)
    
    question = json["question"]
    thisQuestion = Question.get(question)[0]
    content = json["content"]
    isSolution = True 

    newAnswer = Answer.noID(None, thisUser, thisQuestion, None, content, isSolution, ACTIVE)
    newAnswer.add()

    return utils.successJson(json)
